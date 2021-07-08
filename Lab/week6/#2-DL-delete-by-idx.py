# Delete an element with int type node value by index in doubly linked list. 
# Try to implement the process in a function. At first, check if the list is empty or not, 
# and then delete, such as list = None<-Head<=>11<=>9<=>13<=>8->None as input,
# output will be None<-Head<=>11<=>9<=>8->None  when calling function dul_LL_delete_index (ls, 2)

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

def dul_LL_delete_index(ls, idx):
  if(idx < 0 or not ls.head):
    print("Please provide valid data to proceed")
    return

  curr = ls.head
  prev = ls.head

  count = 0
  while count <= idx and curr:
    print("count", count)
    if (count == idx):
      if(count == 0):
        print("count = 0")
        ls.head = curr.next
        ls.head.prev = None
        return
      prev.next = curr.next
      curr.next.prev = prev
      return
    prev = curr
    curr = curr.next
    count += 1    
  
  if(idx > count):
    print("Higher index is provided. Pls provide an index in range")
    return

dl1 = DoublyLinkedList()
dl1.append(11)
dl1.append(9)
dl1.append(13)
dl1.append(8)
print("before delete")
dl1.showContens()
dul_LL_delete_index(dl1, 0)
print("after delete")
dl1.showContens()