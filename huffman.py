""" Plik zawierający wszystkie funkcje do kodowania Huffmana,
    NIE ROBIMY TUTAJ NICZEGO Z GUI
"""

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
        self.tree = None
        
    def calculate_frequency(self, text):
        for char in text:
            if char in self.frequency:
                self.frequency[char] += 1
            else:
                self.frequency[char] = 1
        return self.frequency

    def create_tree(self):
        list = sorted(self.frequency.items(), key=lambda x: x[1])
        
        print(list)
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
        if not node.character == '\0':
            return {node.character: binString}
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
            
    def encode(self, text):
        self.calculate_frequency(text)
        self.create_tree()
        print(self.calculate_code(self.tree))
            
        