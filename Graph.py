class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbours(self,neighbour,weight=0):
        self.connectedTo[neighbour] = weight
        
    def __str__(self):
        print "\nThe vertex %s is connected to the vertices %s" % (self.id, str([x.id for x in self.connectedTo]))  
        #print "\nThe vertex %s is connected to the vertices %s" % (self.id, self.connectedTo.keys())  
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id
        
    def getWeight(self,neighbour):
        return self.connectedTo[neighbour]
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.noOfVertices = 0
        
    def addVertex(self,key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        self.noOfVertices += 1
        return newVertex
        
    def getVertex(self,key):
        return self.vertices.get(key,None)
        
    def __contains__(self,vertex):
        return vertex in self.vertices
        
    def addEdge(self,start,end,weight=0):
        if start not in self.vertices:
            self.vertices[start] = self.addVertex(start)
        if end not in self.vertices:
            self.vertices[end] = self.addVertex(end)    
        self.vertices[start].addNeighbours(self.vertices[end],weight)
        
    def getVertices(self):
        return self.vertices.keys()
        
    def __iter__(self):
        return iter(self.vertices.values())
        
def main():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
        print g.vertices
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
            
if __name__ == '__main__':
    main()