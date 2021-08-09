# The arithmetic expression can be converted to a binary tree structure, 
# where all leaves are numbers and all inner-node labels are operators
#  (just considering 7 operations: +, -, *, /, //, %, **),
#  such as the following binary tree for the expression: 3 + ((5+9)*2).
#  Define a function/method eval(t) to calculate the expression value denoted by

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def process(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b
    if operator == '//':
        return a // b
    if operator == '%':
        return a % b
    if operator == '**':
        return a ** b

  
def isLeafNode(node):
    return node.left is None and node.right is None

def eval(t):
    if root is None :
        print("Please provide a valid binary tree with operands")
        return 0
    def evaluate(root):
    
        if isLeafNode(root):
            return int(root.data)
    
        a = evaluate(root.left)
        b = evaluate(root.right)
        
        print(root.data, a, b)
        return process(root.data, a, b)

    return evaluate(t)

root = Node('+')
root.left = Node(3)
root.right = Node('*')

root.right.left = Node('+')
root.right.right = Node(2)

root.right.left.left = Node(5)
root.right.left.right = Node(9)

print(eval(root))