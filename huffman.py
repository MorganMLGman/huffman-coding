""" Plik zawierający wszystkie funkcje do kodowania Huffmana,
    NIE ROBIMY TUTAJ NICZEGO Z GUI
"""


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
class Huffman(object):     
    def __init__(self) -> None:
        self.huffmanCode = {}
        self.frequency = {}
    
    def __str__(self):
        ret = " Char | Frequency | Huffman code "
        ret += "\n---------------------------------"
        for (char, frequency) in self.frequency:
            ret += f"""\n '{char}' | {frequency}% | '{self.huffmanCode[char]}'"""
        
        return ret
    
    def calculate_freq(self, text: str) -> dict:
        freq = {}
        
        for c in text:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return freq
    
    def code_tree(self, node: NodeTree, left=True, binString='') -> dict:
        if type(node) is str:
          return {node: binString}
      
        (l, r) = node.children()
        ret = dict()
        ret.update(self.code_tree(l, True, binString + '0'))
        ret.update(self.code_tree(r, False, binString + '1'))
        return ret
    
    def run(self, text: str) -> dict:        
        freq = self.calculate_freq(text)
        self.frequency = freq
        nodes = freq
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
            
        huffmanCode = self.code_tree(nodes[0][0])
        
        self.huffmanCode = huffmanCode
        return huffmanCode
    
    def drawGraph(self):
        