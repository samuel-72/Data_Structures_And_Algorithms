class BinHeap():
    
    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i//2]
                self.heaplist[i//2] = tmp
        i = i // 2
        
    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize += 1
        self.percUp(self.currentsize)
    
    def percDown(self,i):
        while i*2 < self.currentsize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
        pass
        
    def minChild(self,i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1
    
    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.heaplist.pop()
        self.currentsize -= 1
        self.percDown(1)
        return retval