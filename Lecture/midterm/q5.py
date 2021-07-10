# . Linked list can be built in an array data type as the following example, in which each element is a class object with two components, data and index pointing to next element in the array.  
 
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
# t
# Write a function/method to insert an element by index to linked list in array structure with a char type node. For example, given ls = Head->S->t->i->n->g->None, the new one will be Head->S->t->r->i->n->g->None by calling function insertElem(ls, 3, 'r') as shown in the figure below

import numpy as np

class Node:
  def __init__(self, data, idx):
    self.data=data
    self.idx=idx

class LLNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    newNode = LLNode(data)
    if self.head is None:
      self.head = newNode
      return

    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = newNode


def findHeadNode(ls):
  for i in ls:
    if(i.data == 'head' or i.idx == 1): #either the data is head or next pointer is the very next index
      return i

def findTailNode(ls):
  for i in ls:
    if(i.idx == None): #either the data is head or next pointer is the very next index
      return i

def getPreviousPointer(ls, currIdx): #returns the node pointing to the current index node
  pointerIdx = None
  for i in range(0, len(ls)):
    if (ls[i].idx == currIdx): #either the data is head or next pointer is the very next index
      pointerIdx = i
      return i
  return pointerIdx

def rev(ls):
  if (not(len(ls))):
    return

  head = ls[0]
  newLs = []
  if (head.data.lower() != 'head'):
    head = findHeadNode(ls)
  
  for i in range (0, (len(ls))):
    prevIdx = getPreviousPointer(ls, i)

    if (prevIdx is None):
      newLs.append(ls[i])
    
    elif(prevIdx == 0): #pointing back to head
      newNode = Node(ls[i].data, None) 
      newLs.append(newNode)
    
    elif (not (ls[i].idx) and ls[i].data):
      newNode = Node(ls[i].data, prevIdx) 
      newLs.append(newNode)
      newLs[0].idx = i

    elif(ls[i].data is not None):
      newNode = Node(ls[i].data, prevIdx)
      newLs.append(newNode)

  ll = printArrIdxAsLinkedList(newLs)
  showContentsInLinkedList(ll)


def printArrIdxAsLinkedList(ls): #coverts the reversed array into linked list
  if(not len(ls) or not ls[0].idx):
    print("Invalid list")
    return
  
  curr = ls[0] #head
  newList = SinglyLinkedList()
  while curr:
    newList.append(curr.data)
    if(curr.idx):
      curr = ls[curr.idx]
    else:
      curr = None
  
  return newList

def showContentsInLinkedList(ls): #prints all the data in linked list
  if not ls or not ls.head:
    return
  else:
    contents = []
    curr = ls.head
    while curr:
      contents.append(curr.data)
      curr = curr.next
    print("contents in Linked list are", contents)
elm0=Node("head",1)
elm1=Node("S",2)
elm2=Node("t",3)
elm3=Node("i",4)
elm4=Node("n",5)
elm5=Node("g",None)

ls=np.array([elm0, elm1, elm2, elm3, elm4, elm5])
print(ls[2].data)

reversedList = rev(ls)


ls1 = Node("head", 1)
ls2 = Node(11, 2)
ls3 = Node(12, 3)
ls4 = Node(13, 4)
ls5 = Node(14, 6)
ls6 = Node(None, None)
ls7 = Node(15, None)

ls2 = np.array([ls1, ls2, ls3, ls4, ls5, ls6, ls7])

reversedList2 = rev(ls2)






