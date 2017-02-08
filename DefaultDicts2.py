from collections import defaultdict

d = {}

for name in ['foo', 'bar', 'bars']:
    t = d
    for char in name:
        t = t.setdefault(char,{})
        
print d

"""
d1 = defaultdict(defaultdict)

for name in ['foo', 'bar', 'bars']:
    t1 = d1
    for char in name:
        t1 = t1[char]
print d1



d1 = defaultdict(list)

for name in ['foo', 'bar', 'bars']:
    
    for char in name:
        d1 = d1[char]
        
print d1
"""