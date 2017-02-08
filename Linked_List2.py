class LinkedList(object):
    
    def __init__(self):
        self.root = Node(None)
        self.head = self.root.next
        self.tail = self.root.next
        
    def insert(self,val,pos='end'):
        temp = Node(val)
        if pos == 'end':
            if not self.head:
                self.head = temp
            if not self.tail:
                self.tail = temp
            else:
                self.tail.next = temp
                self.tail = temp
        elif pos == 'beginning':
            self.root.next = temp
            self.root.next.next = self.head
            if not self.tail:
                self.tail = temp
            

            
    def delete(self,val):
        curr = self.root.next
        prev = self.root
        while curr:
            if curr.value == val:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            
           
    def printList(self):
        curr = self.root.next
        while curr:
            print curr.value
            curr = curr.next
        
class Node(object):
    def __init__(self,val):
        self.value = val
        self.next = None
        
def main():
    linkedList = LinkedList()
    linkedList.insert(10)
    linkedList.insert(20)
    linkedList.insert(30)        
    linkedList.insert(5,'beginning')    
    linkedList.delete(20)
    linkedList.printList()    
    linkedList.delete(5)
    linkedList.printList()    
    linkedList.insert(40)
    linkedList.printList()  
    linkedList.delete(40)
    linkedList.printList()    
    
if __name__ == '__main__':
    main()