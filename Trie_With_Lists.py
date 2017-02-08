class TrieNode(object):

    __slots__ = ['char','count','children','isWord']
    
    def __init__(self,char):
        self.char = char
        self.count = 0
        self.children = []
        self.isWord = False
        
    def getNode(self,char):
        for child in self.children:
            if child.char == char:
                return child
        return None
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode('*')
        
    def addWord(self,word):
        curr = self.root
        for char in word:
            next_node = curr.getNode(char)
            if not next_node:
                next_node = TrieNode(char)
                curr.children.append(next_node)
            next_node.count += 1
            curr = next_node
        curr.isWord = True
            
    def findWord(self,word):
        curr = self.root
        for char in word:
            next_node = curr.getNode(char)
            if not next_node:
                return 0
            curr = next_node
        return curr.count

trie = Trie()
n = int(raw_input("Enter the number of operations to be performed : ") )               
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        trie.addWord(contact)
    elif op == "find": 
        print trie.findWord(contact)