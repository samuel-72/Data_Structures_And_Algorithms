class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def printLL(self):
        currentNode = self.head
        while currentNode:
            print "\nData : %d\tNode at address : %s\tNext node : %s\n" % (currentNode.data,currentNode,currentNode.next)
            currentNode = currentNode.next
            
    def detectLoop(self):
        sp = fp = self.head
        while sp and sp.next and fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                print "\nLoop detected in the linked list.\n"
                return
        if sp == fp:
            print "\nLoop detected in the linked list.\n"
            return
        print "\nNo loop in the linked list.\n"
        return

    def detectAndRemoveLoop(self,method):
        sp = fp = self.head
        while sp and sp.next and fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                print "\nLoop detected in the linked list.\n"
                self.removeLoop(sp)
                return
        if sp == fp:
            print "\nLoop detected in the linked list.\n"
            if method == 'm1':
                self.removeLoop(sp)
            else:
                self.removeLoopBetterWay(sp)
            return
        print "\nNo loop in the linked list.\n"
        return
            
    def removeLoop(self,loop_node):
        ptr1 = self.head
        ptr2 = loop_node
        while 1:
            while ptr2.next != ptr1 and ptr2.next != loop_node:
                ptr2 = ptr2.next
            if ptr2.next == ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None
        print "\nThe loop has been detected and removed.\n"
            
    def removeLoopBetterWay(self,loop_node):
        ptr1 = ptr2 = loop_node
        # Get k - the number of nodes in the loop
        k = 1
        while ptr1.next != ptr2:
            ptr1 = ptr1.next
            k += 1
        ptr1 = ptr2 = self.head
        # Advance one pointer to k nodes from the head
        for i in xrange(k):
            ptr2 = ptr2.next
        # Move both the pointers now, when they meet its the loop head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        # Get the pointer to the last node now and set it to None
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None
                                            
def main():
    # Create the LL
    linkedlist1 = LinkedList()
    # Insert values in LL
    for i in xrange(1,5):
        linkedlist1.insert(10*i)
    # Print the LL
    linkedlist1.printLL()
    # Detect if there is a loop
    linkedlist1.detectLoop()
    # Create a LL with loops
    linkedlist2 = LinkedList()
    linkedlist3 = LinkedList()
    # Insert values in LL
    for i in [6,5,4,3,2,1]:
        linkedlist2.insert(10*i)
        linkedlist3.insert(10*i)
    # Create loop
    # LL now is 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> 90
    # linkedlist2.head.next.next.next.next.next = 60, linkedlist2.head.next.next = 30
    linkedlist2.head.next.next.next.next.next = linkedlist2.head.next.next
    linkedlist3.head.next.next.next.next.next = linkedlist3.head.next.next
    # Can print to verify that there is a loop
    #linkedlist2.printLL() 
    # Detect if there is a loop and remove it
    linkedlist2.detectAndRemoveLoop('m1')
    linkedlist3.detectAndRemoveLoop('m2')
    # Print the LL
    linkedlist2.printLL()
    linkedlist3.printLL()    
    
    
if __name__ == '__main__':
    main()