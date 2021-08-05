# Program for pre-order traversal (data, left, right)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def isNumberExists(root, n):
     
    if root is None:
        return
 
    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack) > 0):
         
        node = nodeStack.pop()
        if node.data == n:
            return True
        
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
 
    return False


##  level 1 -----------------
root = Node(10)
## level 2 -----------------
root.left = Node(11)
root.right = Node(12)
## level 3
root.left.left = Node(13)
root.left.right = Node(14)
root.right.left = Node(15)
root.right.right = Node(16)

## level 4
root.left.left.left = Node(17)
root.left.left.right = Node(18)
root.right.left.right = Node(22)
root.right.right.right = Node(24)

print("Results by DLR traversal (Preordered)")

print("22 Exists", isNumberExists(root, 22))
print("1 exists", isNumberExists(root, 1))
 
