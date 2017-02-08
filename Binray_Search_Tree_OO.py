class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size
        
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
        
    def put(self,key,val):
        if not self.root:
            self.root = TreeNode(key,val)
        else:
            self._put(key,val,self.root)
        self.size = self.size + 1
            
    def _put(self,key,val,currentNode):
        if currentNode.key > key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        elif currentNode.key <= key:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                
    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return  res.payload       
            else:
                return None
        else:
            return None    
            
            
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key >= key:
            return self._get(key,currentNode.leftChild)
        elif currentNode.key < key:
            return self._get(key,currentNode.rightChild)       
        
    def __getitem__(self,key):
        return self.get(key)         
        
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
            
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self.get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("\nThe key to be deleted is not found")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            return None
            
    def remove(self,currentNode):
        """
        Case 1 : The node to be removed is a leaf node with no children
        Case 2 : The node to be removed has either a left or right child but not both
        Case 3 : The node to be removed has both left and right children
        """
        # Case 1 - No children 
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
            
        # Case 2 - Has either left child or right child only
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                             currentNode.leftChild.payload,
                             currentNode.leftChild.leftChild,
                             currentNode.leftChild.rightChild)
            
        
            elif currentNode.hasRightChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                            currentNode.rightChild.payload,
                            currentNode.rightChild.rightChild,
                            currentNode.rightChild.rightChild)
            
            # Case 3 - Has both left and right children
            elif currentNode.hasBothChildren():
                succ = currentNode.findSuccessor()
                succ.spliceOut()
                currentNode.key = succ.key
                currentNode.payload = succ.payload

    def checkBST(self):
        if not self.root:
            return True
        return self._checkBST(self.root,float('-inf'),float('inf'))

    def _checkBST(self,currentnode,minValue,maxValue):
        if not currentnode:
            return True
        if currentnode.payload >= minValue and currentnode.payload < maxValue:
            return self._checkBST(currentnode.leftChild,minValue,currentnode.payload) and self._checkBST(currentnode.rightChild,currentnode.payload+1,maxValue)
        else:
            return False
            
    def inOrderTraversal(self):
        #if not self.root:
        #    return 
        self._inOrderTraversal(self.root)
        
    def _inOrderTraversal(self,currentNode):
        if not currentNode:
            return
        if currentNode.hasLeftChild():
            self._inOrderTraversal(currentNode.leftChild)
        print currentNode.payload
        if currentNode.hasRightChild():
            self._inOrderTraversal(currentNode.rightChild)
            
        
class TreeNode:
    
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftChild
        
    def hasRightChild(self):
        return self.rightChild
        
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
        
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
              
        
    def isRoot(self):
        return not self.parent
        
    def isLeaf(self):
        return not (self.leftChild or self.righChild)
        
    def hasAnyChildren(self):
        return (self.leftChild or self.righChild)
        
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
        

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
    def findSuccessor(self):
        """
        Case 1 - The node 'has' a right child. Use same principle as inorder traversal to find the min for all nodes under this right child
        Case 2 - The node 'is' the left child of its parent. If the node has a parent then that will be the successor, else the successor of the parent is the successor
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
            
    def findMin(self):
        """
        Recursive approach
        if self.isLeaf():
            return self
        else:
            self.leftChild.findMin()
        """
        # Iterative approach
        current = self
        while current.hasLeftChild():
            current = current.leftChild 
        return current
        
        
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                   self.parent.leftChild = None
            else:
                   self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                   if self.isLeftChild():
                      self.parent.leftChild = self.leftChild
                   else:
                      self.parent.rightChild = self.leftChild
                   self.leftChild.parent = self.parent
            else:
                   if self.isLeftChild():
                      self.parent.leftChild = self.rightChild
                   else:
                      self.parent.rightChild = self.rightChild
                   self.rightChild.parent = self.parent
                   
                   
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])

# Checking for BST correctness - Begins
nos = BinarySearchTree()
nos.put(10,10)
nos.put(9,9)
nos.put(20,20)
nos.put(4,4)
nos.put(5,5)
nos.put(11,11)
nos.put(22,22)

print nos.inOrderTraversal()

print nos.checkBST()

nos[9] = 111

print nos.checkBST()
# Checking for BST correctness - Ends