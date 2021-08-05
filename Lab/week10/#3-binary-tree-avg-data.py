# Program for pre-order traversal (data, left, right)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def getAverageInBinaryTree(root):
     
    if root is None:
        return
    total = 0
    count = 0
    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack) > 0):
         
        node = nodeStack.pop()
        if node.data:
            total += node.data
            count += 1
        
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
 
    return total/count


#------ level 1 -----------------
root = Node(1)
#------ level 2 -----------------
root.left = Node(2)
root.right = Node(3)
#------ level 3 -----------------
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#------ level 4 -----------------
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left.right = Node(10)
root.right.right.right = Node(11)


print(getAverageInBinaryTree(root)) #66/11 = 6
 
