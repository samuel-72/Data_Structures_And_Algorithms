from collections import deque

q = deque([1,2,3,4])

print q

q.appendleft(0)

q.append(5)

print q

q.rotate(1)

print q