# 2. Assuming that there are two circular linked lists l & m with char type node value from 
# a-zA-Z in non-descending sequence, find a function/method to extract common node 
# values from both, and generate a new circular list without duplicated one

# 	Hint: take question 4 in HW#3 as reference 

from typing import final


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList():
  def __init__(self):
    self.head = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode

    else:
      curr = self.head
      while curr.next is not self.head:
        curr = curr.next
      curr.next = newNode
    newNode.next = self.head

  def showContents(self):
    curr = self.head
    contents = []
    contents.append(curr.data)
    curr = curr.next
    while curr is not self.head:
      contents.append(curr.data)
      curr = curr.next
    print(contents)

def findCommonNodes(l, m):
  if (not(l.head) or not (m.head)):
    print("Please provide non-empty list to proceed")
    return
  
  lData = []
  common = []
  curr = l.head
  lData.append(curr.data)
  curr = curr.next
  while curr is not l.head:
    lData.append(curr.data)
    curr = curr.next

  curr = m.head
  if curr.data in lData and not curr.data in common:
      common.append(curr.data)
  curr = curr.next
  while curr is not m.head:
    if curr.data in lData and not curr.data in common:
      common.append(curr.data)
    curr = curr.next

  print("common nodes are", common)
  finalCL = CircularLinkedList()
  
  for c in common:
    finalCL.append(c)

  return finalCL



l = CircularLinkedList()
l.append('a')
l.append('d')
l.append('e')
l.append('k')
l.append('a')

m = CircularLinkedList()
m.append('a')
m.append('e')
m.append('f')
m.append('k')
m.append('e')
m.append('a')


commonCL = findCommonNodes(l, m)
print("Data in final linked list are")
commonCL.showContents()

