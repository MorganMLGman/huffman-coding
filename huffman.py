""" Plik zawierający wszystkie funkcje do kodowania Huffmana,
    NIE ROBIMY TUTAJ NICZEGO Z GUI
"""
import networkx as nx
from EoN import hierarchy_pos
from matplotlib import pyplot as plt
from time import perf_counter

class Huffman:
    class Node:
        def __init__(self, value = None, character=None, left=None, right=None) -> None:
            self.value = value
            self.character = character
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return '%s_%s' % (self.left, self.right)
        
    def __init__(self) -> None:
        self.frequency = dict()
        self.charCode = dict()
        self.strCode = ""
        self.tree = None
        
    def calculate_frequency(self, text) -> dict:
        for char in text:
            if char in self.frequency:
                self.frequency[char] += 1
            else:
                self.frequency[char] = 1
        return self.frequency

    def create_tree(self) -> Node:
        list = sorted(self.frequency.items(), key=lambda x: x[1])
        nodeC = None
        while len(list) > 1:
            (char1, freq1) = list[0]
            (char2, freq2) = list[1]
            list = list[2:]
            
            if isinstance(char1, str):
                node1 = self.Node(character= char1)
            else:
                node1 = char1
                
            if isinstance(char2, str):
                node2 = self.Node(character= char2)
            else:
                node2 = char2
                            
            nodeC = self.Node(value= (freq1 + freq1), left=node1, right=node2, character="\0")
            list.append((nodeC, freq1 + freq2))
            list = sorted(list, key=lambda x: x[1])        
            
        root = list[0][0]
        self.tree = root
        return root
            
    def calculate_code(self, node: Node, left=True, binString='') -> dict:
        if not isinstance(node, str):
            if not node.character == '\0':
                return {node.character: binString}
        else:
            return {}
        (l, r) = node.left, node.right
        d = dict()
        d.update(self.calculate_code(l, True, binString + '0'))
        d.update(self.calculate_code(r, False, binString + '1'))
        
        if l.character == '\0' and r.character == '\0':
            node.value = l.value + r.value
        elif l.character != '\0' and r.character == '\0':
            node.value = self.frequency[l.character] + r.value
        elif l.character == '\0' and r.character != '\0':
            node.value = l.value + self.frequency[r.character]
        else:
            node.value = self.frequency[l.character] + self.frequency[r.character]
        
        self.charCode = d
        return d
            
    def encode(self, text) -> str:
        startTime = perf_counter()
        tmp = set(text)
        ret = ""
        if len(tmp) == 1:
            self.frequency = {text: 1}
            self.strCode = "0"
            self.charCode = {text: "0"}
            self.tree = self.Node(1, text)
            for _ in range(len(text)):
                ret += "0"
            return ret
        
        self.calculate_frequency(text)
        self.create_tree()
        self.calculate_code(self.tree)
        
        for char in text:
            ret += self.charCode[char]
        
        self.strCode = ret
        print(f"Encode time: {round(perf_counter() - startTime, 5)} seconds")
        return ret
    
    def __add_edge(self, parent: Node, G: nx.DiGraph) -> None:
        if parent is None:
            return
        
        for child in (parent.left, parent.right):
            if child:
                G.add_edge(parent, child)
                self.__add_edge(child, G)
    
    def __get_labels(self, parent: Node, labels) -> None:
        if parent is None:
            return
        
        if parent.character == '\0':
            labels[parent] = parent.value
        else:
            if parent.character in [' ', '\n', '\t']:
                labels[parent] = f"{parent.character!a}"
            else:
                labels[parent] = parent.character
            
        self.__get_labels(parent.left, labels)
        self.__get_labels(parent.right, labels)
    
    def __get_edge_labels(self, parent: Node, edge_labels) -> None:
        if parent is None:
            return
        
        if parent.left:
            edge_labels[parent, parent.left] = "0"
            self.__get_edge_labels(parent.left, edge_labels)
            
        if parent.right:
            edge_labels[parent, parent.right] = "1"
            self.__get_edge_labels(parent.right, edge_labels)
                
    def draw_graph(self, tree: Node = None) -> None:
        startTime = perf_counter()
        plt.figure(figsize=(15, 10))
        G = nx.DiGraph()
        if tree is None:
            if not self.tree is None:
                tree = self.tree
            else: 
                raise ValueError("No tree available")
        self.__add_edge(tree, G)
        
        try:
            pos = hierarchy_pos(G)
        except nx.exception.NetworkXPointlessConcept:
            pos = {tree: (0.5, -0.1)}
        labels = {}
        self.__get_labels(tree, labels)
        edge_labels = {}
        self.__get_edge_labels(tree, edge_labels)           
        nx.draw(G, pos, labels=labels, alpha=0.6)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="C1") 
        plt.savefig("graph.png", dpi=300)
        print(f"Graph time: {round(perf_counter() - startTime, 5)} seconds")