##
# Problem 1: Write a function/method to sort a given linked list with char type node from a-zA-Z. 
# For example, ls = "Head->D->A->C->A->G->NULL", 
# the new linked list should be 
# "Head->A->A->C->D->G->NULL" by calling function srt_LL(ls)
## 


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.count = 0

  def append(self, data):
    newNode = Node(data)
    if (self.head is None):
      self.head = newNode
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode

def srt_LL(ll):
  if (not ll.head or not ll.head.next):
    return ll

  current = ll.head

  while current:
    currentNode = current
    
    while currentNode.next:
      if currentNode.data > currentNode.next.data:
        dataToReplace = currentNode.data
        currentNode.data = currentNode.next.data
        currentNode.next.data = dataToReplace
      
      currentNode = currentNode.next
    current = current.next

def displayContents(ll):
  current = ll.head
  dataList = []
  while current:
    dataList.append(current.data)
    current = current.next
  return dataList

list1 = SinglyLinkedList()
list1.append('D')
list1.append('A')
list1.append('C')
list1.append('A')
list1.append('G')

print("List before sort", displayContents(list1))
srt_LL(list1)
print("List after sort", displayContents(list1))

