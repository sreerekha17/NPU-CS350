# 3.   Implement a pruning function/method which takes in a binary tree t and 
# a depth k, and should return a new tree that is a copy of only the first k levels of t. 
# For example, if t is the tree shown as follows, then pruning(t, 3) should return the new tree

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)
 
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
            
def pruning(root, n):
    if n >= height(root):
        print("Invalid number entered for prune")
        return
    if n < 1:
        print("Level cannot be below 1")
    level = 0
    def pruneIfExists(t, level):
        node = t
        while level <= n:
            if t is None:
                return
            level += 1
            
            left = pruneIfExists(t.left, level)
            right = pruneIfExists(t.right, level)
            if level >= n:
                if t and t.left or t.right:
                    t.left = None
                    t.right = None
                if t and t.left or t.right:
                    t.left = None
                    t.right = None
            return t
    pruneIfExists(root, level)     

# def pruning(root, n):
#     if n >= height(root):
#         print("Invalid number entered for prune")
#         return
#     if n < 1:
#         print("Level cannot be below 1")
#     level = 0
#     def pruneIfExists(t, level):
#         node = t
#         while level <= n:
#             if t is None:
#                 return
#             level += 1
            
#             left = pruneIfExists(t.left, level)
#             right = pruneIfExists(t.right, level)
#             if level >= n:
#                 if t and t.left or t.right:
#                     t.left = None
#                     t.right = None
#                 if t and t.left or t.right:
#                     t.left = None
#                     t.right = None
#             return t
#     pruneIfExists(root, level)


root = Node(10)
root.left = Node(11)
root.right = Node(12)

root.left.left = Node(13)
root.left.right = Node(14)

root.right.left = Node(15)
root.right.right = Node(16)

print("Height before prune", height(root))

pruning(root, 2)

print("Height after prune", height(root))

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.right.data)  #this node gets removed
print(root.right.right)       #this node gets removed


    

    
