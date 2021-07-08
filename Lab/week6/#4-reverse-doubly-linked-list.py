
# Given a doubly linked list with char type node value from a-zA-Z, such as 
# l = None<-Head<=>r<=>A<=>d<=>a<=>R->None, create a function to reverse node sequence.
# For example, None<-Head<=>R<=>a<=>d<=>A<=>r->None will be the result after calling rev_dul_LL (l)

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


  def readFromTail(self):
    contents = []
    last = self.head
    while last.next:
      last = last.next
    
    while last:
      contents.append(last.data)
      last = last.prev
    print("Reading backwards", contents)

def rev_dul_LL(ls):
  if (not ls or ls.head is None):
    print("Reverse cannot be done on empty list")
    return
  
  last = ls.head
  while last.next:
    last = last.next
  
  ls.head = last
  
  while last:
    prev = last.prev
    last.prev = last.next
    last.next = prev
    last = last.next

dl1 = DoublyLinkedList()

dl1.append(1)
dl1.append(2)
dl1.append(3)
dl1.append(4)
dl1.showContens()

print("reversing doubly linked list")
rev_dul_LL(dl1)

print("After reversing doubly linked list")
dl1.showContens()
