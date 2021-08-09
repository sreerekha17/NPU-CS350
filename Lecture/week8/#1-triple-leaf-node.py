# Problem 1.   Write a function/method to make all leaves in a binary tree tripled.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def isLeafNode(node):
    return node and not node.left and not node.right

def tripleLeafNode(root):
     
    if root is None:
        return

    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack) > 0):
         
        node = nodeStack.pop()
        if isLeafNode(node):
            node.data = node.data * 3 
        else:
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)
 


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
# level 4 (leaf nodes)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left.right = Node(10)
root.right.right.right = Node(11)

#Before tripling leaf nodes
print(root.left.left.left.data)    # 8
print(root.left.left.right.data)   # 9
print(root.right.left.right.data)  # 10
print(root.right.right.right.data) # 11

tripleLeafNode(root) 
 
#After replacing leaf nodes
print(root.left.left.left.data)     #24
print(root.left.left.right.data)    #27
print(root.right.left.right.data)   #30
print(root.right.right.right.data)  #33