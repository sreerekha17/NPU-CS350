# Problem 1. Linked list can be built in an array data type as the following example, in which each element is a class object with two components, data and index pointing to next element in the array.  
 
# import numpy as np

# class Node:
#   def __init__(self, data, idx):
#     self.data=data
#     self.idx=idx

# elm0=Node("head",1)
# elm1=Node("S",2)
# elm2=Node("t",3)
# elm3=Node("i",4)
# elm4=Node("n",5)
# elm5=Node("g",None)

# ls=np.array([elm0,elm1,elm2,elm3,elm4,elm5])

# print(ls[2].data)
# 							t

#	Write a function/method to insert an element 
# by index to linked list in array structure with a char type node.
# For example, given ls = Head->S->t->i->n->g->None,
# the new one will be Head->S->t->r->i->n->g->None 
# by calling function insertElem(ls, 3, 'r') as shown in the figure below

# import numpy as np

# class Node:
#   def __init__(self, data, idx):
#     self.data=data
#     self.idx=idx

# elm0=Node("head",1)
# elm1=Node("S",2)
# elm2=Node("t",3)
# elm3=Node("i",4)
# elm4=Node("n",5)
# elm5=Node("g",None)

# ls=np.array([elm0,elm1,elm2,elm3,elm4,elm5])

import numpy as np

class Node:
  def __init__(self, data, idx):
    self.data=data
    self.idx=idx
    
def insertElem(ls, pos, data):
  if(ls is None or not(len(ls)) or pos < 1):
    print("Invalid list or index ")
    return ls
  if pos > len(ls)-1:
    print("Higher index provided. Please enter a valid index")
    return ls
  currentNode = ls[0]
  newNode = Node(data, pos)

  ls = np.append(ls, newNode)
  index = 0
  while currentNode:
    if (currentNode.idx == pos):
      nextListPointer = currentNode.idx
      currentNode.idx = len(ls) - 1 #pointing to the last added node
      newNode.idx = nextListPointer
      return ls
    elif index == pos: #when position is the last index
      print("last pos", pos, currentNode.data, currentNode.idx)
      currentNode.idx = len(ls) - 1
      newNode.idx = None
      return ls
    currentNode = ls[currentNode.idx]
    index += 1

  return ls

def showContents(ls):
  if not len(ls):
    print("Empty list given")
    return
  current = ls[0]
  items = []
  while current:
    items.append(current.data)
    current = current.idx and ls[current.idx]
  print(items)

elm0=Node("head",1)
elm1=Node("S",2)
elm2=Node("t",3)
elm3=Node("i",4)
elm4=Node("n",5)
elm5=Node("g",None)

ls=np.array([elm0,elm1,elm2,elm3,elm4,elm5])

ls = insertElem(ls, 3, 'r')

showContents(ls)