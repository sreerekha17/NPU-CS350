# Find a program to sort int type node value in doubly linked list.
# If the input argument in function is like lst = None<-Head<=>2<=>0<=>2<=>0->None,
# the new doubly linked should be None<-Head<=>0<=>0<=>2<=>2->None after function call srt_dul_LL (lst)


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)

    if (self.head is None):
      self.head = newNode
      return
    
    curr = self.head
    while curr.next:
      curr = curr.next

    curr.next = newNode
    newNode.prev = curr

  def showContens(self):
    contents = []
    curr = self.head
    while curr:
      contents.append(curr.data)
      curr = curr.next
    print("from head", contents)

def srt_dul_LL(ls):
  if(not(ls) or ls.head is None):
    print("Requires non-empty linked list to proceed with sort")
    return
  
  curr = ls.head

  while curr:
    next = curr.next
    while next:
      if curr.data > next.data:
        temp = curr.data
        curr.data = next.data
        next.data = temp
      next = next.next
    curr = curr.next



dl1 = DoublyLinkedList()
srt_dul_LL(dl1)

dl1.append(2)
dl1.append(0)
dl1.append(2)
dl1.append(0)

dl1.showContens()
srt_dul_LL(dl1)
dl1.showContens()