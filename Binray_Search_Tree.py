class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def push(self,node,data):
        if node.data > data:
            if not(node.left):
                node.left = BST(data)
            else:
                node.push(node.left,data)
        elif node.data <= data:
            if not(node.right):
                node.right = BST(data)
            else:
                node.push(node.right,data)

    def search(self,node,searchData):
        if node.data == searchData:
            print "\nData : %s\tFound at node : %s\n" % (node.data,node)
            return 
        elif node.data <= searchData:
            if not(node.right):
                print "\nData not found.\n"     
                return           
            else:
                self.search(node.right,searchData)
        elif node.data > searchData:
            if not(node.left):
                print "\nData not found.\n"  
                return              
            else:
                self.search(node.left,searchData)
        
    def printInOrder(self,node):
        if not(node):
            return
        node.printInOrder(node.left)
        print node.data
        node.printInOrder(node.right)
        

            
def main():
    bst = BST(3)
    # Insert data into BST
    bst.push(bst,7)
    bst.push(bst,1)
    bst.push(bst,5)    
    bst.push(bst,8)
    bst.push(bst,4)        
    # Print In Order
    bst.printInOrder(bst)         
    # Search for 8
    bst.search(bst,5)     
    bst.search(bst,1)     
    bst.search(bst,3)     
    bst.search(bst,4)
    bst.search(bst,0)
    #print bst.data, bst.left.data , bst.right.data                     

if __name__ == '__main__':
    main()
