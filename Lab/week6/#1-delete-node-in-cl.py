
# Write two functions to delete an element in circular linked list by index or value. 
# In the beginning of process, each function needs to check if circular linked list is empty or not.
#  If empty, print message, such as "not necessary to delete anything".
#  For instance, given circular linked list ls = Head->13->12->15->14->Head, 
# after calling function cirLL_delete_key (ls, 15), the result should be Head->13->12->14->Head. 
# If cirLL_delete_index (ls, 0) is called, 
# you will get Head->12->15->14->Head


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if( self.head is None):
      self.head = newNode
    else:
      curr = self.head
      while curr.next is not self.head:
        curr = curr.next
      curr.next = newNode
    newNode.next = self.head

  def showContents(self):
    if(not self.head):
      print("Empty linked list")
      return
    contents = []
    curr = self.head
    contents.append(curr.data)
    curr = curr.next
    while curr != self.head:
      contents.append(curr.data)
      curr = curr.next
    print(contents)
  
  def isCircularList(self):
    if(self.head is None):
      print("Empty list")
      return
    
    curr = self.head
    while curr:
      if(curr.next is self.head):
        return True
      else:
        curr = curr.next
    return False
def cirLL_delete_key(list, nodeData):
  if(not list or not list.head or not nodeData):
    print("not necessary to delete anything")
    return

  curr = list.head
  prev = list.head
  if(curr.data == nodeData):
    newHead = curr.next
    list.head = newHead
    while curr.next is not list.head:
      curr = curr.next
    curr.next = list.head
  curr = curr.next
  while curr is not list.head:
    if(curr.data == nodeData):
      if(curr.next is list.head): #for last node
        prev.next = list.head
      else:
        prev.next = curr.next
    prev = curr
    curr = curr.next      


def cirLL_delete_index(list, idx):
  if(not list or not list.head or idx < 0 ):
    print("not necessary to delete anything")
    return

  curr = list.head

  if (idx == 0):
    list.head = curr.next
    while curr.next is not list.head:
      curr = curr.next
    curr.next = list.head
    return
  
  prev = list.head
  curr = list.head.next
  count = 1

  while count <= idx and curr:
    if (idx == count):
      if (curr.next == list.head): #last item connecting to head
        prev.next = list.head
      else:
        prev.next = curr.next
      return
    prev = curr
    curr = curr.next
    count += 1

  print("index given is invalid, Please provide an index in range to proceed")

cl1 = CircularLinkedList()
cl1.append(10)
cl1.append(20)
cl1.append(30)
cl1.append(40)
cl1.append(50)
cl1.append(40)

cl1.showContents()

cirLL_delete_key(cl1, 40)
cl1.showContents()

cirLL_delete_index(cl1, 3)
cl1.showContents()
