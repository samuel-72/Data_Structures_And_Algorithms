class Binary_Tree:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,data,side='left'):
        if side == 'left':
            if not(self.left):
                self.left = Binary_Tree(data)
            else:
                temp = Binary_Tree(data)
                temp.left = self.left
                self.left = temp
        elif side == 'right':
            if not(self.right):
                self.right = Binary_Tree(data)
            else:
                temp = Binary_Tree(data)
                temp.right = self.right
                self.right = temp

    def getLeftChild(self,node):
        return node.left

    def getRightChild(self,node):
        return node.right

    def setLeftChild(self,node,data):
        node.left.data = data

    def setRightChild(self,node,data):
        node.right.data = data
                                        
    def getRootVal(self):
        return self.data
        
    def setRootVal(self,data):
        self.data = data
                                                        
    def inOrderTraversal(self,node):
        if not(node):
            return
        self.inOrderTraversal(node.left)
        print node.data
        self.inOrderTraversal(node.right)          
    
    def preOrderTraversal(self,node):
        if not(node):
            return
        print node.data
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)        

def main():
    # Create tree and insert values
    r = Binary_Tree('a')
    r.insert('d','left')  
    r.insert('b','left')
    r.insert('c','right')
    # Print in order traversal
    print "\nIn-Order Traversal : \n",     r.inOrderTraversal(r)
    # Print pre-order traversal
    print "\nPre-Order Traversal : \n", r.preOrderTraversal(r)
    # Manipulate value
    print(r.getRightChild(r))
    print(r.getRightChild(r).getRootVal())
    r.getRightChild(r).setRootVal('hello')
    print(r.getRightChild(r).getRootVal())
    # Print in order traversal
    print "\nIn-Order Traversal : \n",     r.inOrderTraversal(r)
            
if __name__ == '__main__':
    main()
