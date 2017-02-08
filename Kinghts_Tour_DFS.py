from pythonds.graphs import Graph, Vertex 
from pythonds.basic import Queue


def posToNodeId(row,col,boardSize):
    """
    This function takes as input the row no, column no and boardsize and returns a no which is the the id of the square. 
    For a 64 square board the Id ranges from 0 - 63 and is calculated as (row * boardsize) + column
    """
    return (row * boardSize) + col

def genLegalMoves(row,col,boardSize):
    """
    This function takes a square Id and computes all possible moves for a Knight from that square
    """
    moveOffsets = [ (-1,2), (-1,-2), (1,2), (1,-2),
                    (-2,1), (-2,-1), (2,1), (2,-1)
                  ] # Because a Knight can move either 1 row and 2 columns or 2 rows and 1 column on a board
    newPositions = []
    for i in moveOffsets:
        newX = row + i[0]
        newY = col + i[1]
        if checkLegalityOfMove(newX,newY,boardSize):
            newPositions.append((newX,newY))
    return newPositions
        

def checkLegalityOfMove(row,col,boardSize):
    """
    This function checks if the move being passed as input is legal, i.e., it is within the board boundaries. 
    """
    if row >=0 and row < boardSize and col >=0 and col < boardSize:
        return True
    return False      
                  
def knightGraph(boardSize):
    """
    This function takes as input the boardsize (Eg : 8 for a 64 square - 8 x 8 board) and creates a graph of all possible moves for a knight from each square on the board
    Each square on the board is represented as a number from 0 - 63
    """
    ktGraph = Graph()
    for row in range(boardSize):
        for col in range(boardSize):
            posId = posToNodeId(row,col,boardSize)
            newPositions = genLegalMoves(row,col,boardSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],boardSize)
                ktGraph.addEdge(posId,nid)
    return ktGraph
    

def bfs(g,start):
    start.setDistance(0)
    start.setPred('None')
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        current = vertQueue.dequeue()
        for neighbour in current.getConnections():
            if neighbour.getColor() == 'white':
                neighbour.setColor('gray')
                neighbour.setDistance(current.getDistance() + 1)
                neighbour.setPred(current)
                vertQueue.enqueue(neighbour)
        current.setColor('black')

def orderByAvail(n):
    """
    This function takes as input a vertex and finds the neighbour with least no of squares to move and returns that neighbour
    """
    resultList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resultList.append((c,v))
    resultList.sort(key=lambda x: x[0])
    return [x[1] for x in resultList]
        
                

def knightTour(n,limit,path,u):
    
    if n >= limit:
        done = True
    else:
        path.append(u)
        u.setColor('gray')
        #neighbours = list(u.getConnections())
        neighbours = orderByAvail(u)
        done = False
        i = 0
        print "Current Node : %s . n : %s limit : %s" % (u.id,n,limit)
        while i < len(neighbours) and not done:
            if neighbours[i].getColor() == 'white':
                done = knightTour(n+1,limit,path,neighbours[i])
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    print "Path for now : %s\nSorted : %s\n" % (str([x.id for x in path]), sorted([x.id for x in path]))
    return done

def knightTourBookImplementation(n,limit,path,u):
    print "Current Node : %s . n : %s limit : %s" % (u.id,n,limit)
    u.setColor('gray')
    path.append(u)
    print "Path for now : %s" % str([x.id for x in path])
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            #print "The node %s has neighbours %s" % (u.id, str([x.id for x in nbrList]))
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, limit, path, nbrList[i])
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
        print "Path: %s\n\n" % str([x.id for x in path])
        print sorted([x.id for x in path])
    return done        
#"""



g = Graph()
for i in (['A','B','C','D','E','F']):
#for i in ([0,1,2,3,4,5]):
   g.addVertex(i)

g.addEdge('A','B',0)
g.addEdge('A','D',0)
g.addEdge('B','C',0)
g.addEdge('B','D',0)
g.addEdge('D','E',0)
g.addEdge('E','F',0)
g.addEdge('E','B',0)
g.addEdge('F','C',0)
path = []
#print knightTour(1,6,path,g.vertices['A'])

bSize = 8
knightSquares = knightGraph(bSize)
"""
print str([x for x in knightSquares.vertices])
for v in knightSquares:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
"""
print knightTour(1,(bSize**2),path,knightSquares.vertices[0])
#print knightTourBookImplementation(1,(bSize**2),path,knightSquares.vertices[0])