from collections import defaultdict

trie = defaultdict(lambda: dict)

args = ['viks','daks']

for word in args:
    if type(word) != str:
        raise TypeError("Trie only works on str!")
    temp_trie = trie
    for letter in word:
        temp_trie = temp_trie[letter]
        #print temp_trie
    temp_trie = temp_trie.setdefault('_end_', '_end_')
    
print trie

"""
print "Printing answer"
d = {}
args = ['viks']
temp = d
for char in args:
    temp = temp.setdefault(char, {})
    print temp
temp = temp.setdefault('_end_', '_end_')
print "Ans",d
"""