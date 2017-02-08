import os

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

t_matrix = [ [row[i] for row in matrix] for i in range(len(matrix[0])) ]

for n,row in enumerate(matrix):
    print row, n 
    
    
for n,row in enumerate(t_matrix):
    print row, n     

nm = [ [ 0 for col in range(3) ] for row in range(4) ]

print zip(*matrix)

d = {'arg1':'one','arg2':'two'}

def unpackingExample(arg1='nothing',arg2='default'):
    print "Printing arg1 : %s\nPrinting arg2 : %s" % (arg1,arg2)
unpackingExample()
unpackingExample(**d)

zipped = [(1, 4,10), (2, 5,8,9), (3, 6,7)]

print zip(*zipped)

print [ [row[col] for row in zipped if row[col] ] for col in range(min([len(row) for row in zipped ])) ]


from itertools import count,cycle,islice

cnt = count(5.0)

print "Count : ", next(cnt)
print "Count : ", next(cnt)

colors = cycle(['red','green','blue'])

print "Cycle of colors : ", next((colors))
print "Cycle of colors : ", next((colors))
print "Cycle of colors : ", next((colors))
print "Cycle of colors : ", next((colors))

print "Slice of colors : ", [ x for x in islice(colors,0,6)] 


def fib():
    prev = 0
    curr = 1
    while True:
        yield curr
        prev,curr = curr,curr+prev

f = fib()
print [ next(f) for i in range(10) ]
for i in range(10):
    print next(f)
    

    
with open(os.getcwd() + '\\cubing.py','r') as f:
    try:
        line = f.readline()
        lineNo = 1
        while line:
            print "Line : %d\tContent - %s" % (lineNo,line)
            lineNo += 1
            line = f.readline()
    except Exception as E:
        print E