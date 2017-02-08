class BinHeap:
    
    def __init__(self):
        self.currentSize = 1
        self.heap = [0]

    def percUp(value,i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i//2]:
                temp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2
        return
    
    
    def insert(self,value):
        self.heap[self.currentsize] = value
        self.currentSize += 1
        self.percUp(value,self.currentsize)
        return 
    
    def minChild(self,i):
        if i*2 +1 > self.currentSize:
            return i*2
        if self.heap[i*2] < self.heap[i*2+1]:
            return i*2
        else:
            return i*2+1
    
    def percDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[mc]
                self.heap[mc] = self.heap[i]
                self.heap[i] = temp
            i = mc
            
     
    
    def deleteMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.percDown(1)
        return retval
        
    def buildHeap(self,listOfValues):
        self.heap = [0] + listOfValues[:]
        self.currentSize = len(listOfValues)
        i = len(listOfValues)//2
        while i > 0:
            self.percDown(i)
            i -= 1
        
def main():
    bh = BinHeap()
    bh.buildHeap([9,5,6,2,3])

    print(bh.deleteMin())
    print(bh.deleteMin())
    print(bh.deleteMin())
    print(bh.deleteMin())
    print(bh.deleteMin())
        
if __name__ == '__main__':
    main()