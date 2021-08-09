# Define a function or write a method in a class to 
# create Fibonacci tree like the examples as shown in the following two cases when it is invoked, 
# like Fib_tree(5) and Fib_tree(8)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def fibTree(n):
    root = Node(5)

    def treeGenerator(n):
        if n < 2:
            return Node(n)
        left = treeGenerator(n-1)
        right = treeGenerator(n-2)
        newNode = Node(left.data + right.data)
        newNode.left = left
        newNode.right = right

        return newNode

    return treeGenerator(n)

root = FibTree(5)
print(root.data)                       #5
print(root.left.data)                  #3
print(root.right.data)                 #2
print(root.left.left.data)             #2
print(root.left.right.data)            #1

print(root.left.right.left.data)
print(root.left.right.right.data)

print(root.left.left.left.data)
print(root.left.left.right.data)