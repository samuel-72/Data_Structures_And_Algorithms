from collections import defaultdict
class TrieNode(object):
    __slots__ = ['num_usage','children']
    def __init__(self):
        self.num_usage = 0
        self.children = defaultdict(TrieNode)
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,contact):
        node = self.root
        for char in contact:
            #print node, char
            node = node.children[char]
            #print node, char
            node.num_usage += 1

    def find(self,contact):
        node = self.root
        #print node.children
        for char in contact:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.num_usage


trie = Trie()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    else:
        print trie.find(contact)
    