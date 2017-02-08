from collections import defaultdict

def fix(f):
    return lambda *args, **kwargs: f(fix(f), *args, **kwargs)

d1 = fix(defaultdict)()

for name in ['foo', 'bar', 'bars']:
    t1 = d1
    for char in name:
        t1 = t1[char]

def sq(*args):
    return 2
    
def fix2(f):
    return lambda *args, **kwargs: f(fix(f), *args, **kwargs)

#print fix2(defaultdict)()


#f = lambda *args, **kwargs: f(fix2(f), args, kwargs)

#print f('required', 3, 'optional-positional', kwargs = 'keyword_args')

print fix2(sq)()

f = lambda x, z, y=3 : x * y + z

print f(2,z=8)
print f(2,5,8)