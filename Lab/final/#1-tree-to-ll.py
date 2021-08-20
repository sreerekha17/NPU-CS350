
# Write a function conv(tree) to convert char type node in a binary tree as follows to linked list Head ->'a'->'+' ->'b' ->'*'->'c' ->'-' ->'d' ->'-' ->'e' ->'/' ->'f '-> None as return value by inordered traversal.

class LLNode:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        new_node = LLNode(new_data)

        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

def createLLFromArray(arr):
    if arr is None or not(len(arr)):
        return
    ll = LinkedList()

    for i in range(-1, -(len(arr) +1), -1):
        ll.push(arr[i])
    return ll

    
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def getNodeDataByInOrder(root):
    charNodes = []
    current = root
    stack = []
    done = 0
     
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            charNodes.append(current.data)

            current = current.right
 
        else:
            break
      
    return charNodes

root = Node('-')
#------ level 2 -----------------
root.left = Node('+')
root.right = Node('/')
#------ level 3 -----------------
root.left.left = Node('a')
root.left.right = Node('*')
root.right.left = Node('e')
root.right.right = Node('f')
#------ level 4 -----------------
root.left.right.left = Node('b')
root.left.right.right = Node('-')
#------ level 5 -----------------
root.left.right.right.left = Node('c')
root.left.right.right.right = Node('d')

data = getNodeDataByInOrder(root)
print(data)

createdLinkedList = createLLFromArray(data)
createdLinkedList.printList()
