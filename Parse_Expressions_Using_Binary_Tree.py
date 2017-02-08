from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    tokens = fpexp.split(' ')
    print "\nThe tokens in the expression are : %s\n" % tokens
    currentTree = BinaryTree('')
    pStack = Stack()
    pStack.push(currentTree)
    for token in tokens:
        if token == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif token == ')':
            currentTree = pStack.pop()
        elif token in ['+','-','*','/','%']:
            currentTree.setRootVal(token)
            currentTree.insertRight('')            
            pStack.push(currentTree)            
            currentTree = currentTree.getRightChild()
        elif token.isdigit():
             currentTree.setRootVal(int(token))
             currentTree = pStack.pop()
        else:
            raise ValueError
    return currentTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    
    if leftChild and rightChild:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftChild),evaluate(rightChild))
    else:
        return parseTree.getRootVal()

def printExp(parseTree ):
    exp = ""
    if parseTree:
        exp = '(' + printExp(parseTree.getLeftChild())
        exp = exp + str(parseTree.getRootVal())
        exp = exp + printExp(parseTree.getRightChild()) + ')'
    return exp

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print "\nPrinting Post-Order :\n" , pt.postorder()  #defined and explained in the next section
print "\nPrinting In-Order :\n" , pt.inorder()
print "\nResult of the evaluvation : %s" %evaluate(pt)
print "\nThe original expression : %s" %printExp(pt)