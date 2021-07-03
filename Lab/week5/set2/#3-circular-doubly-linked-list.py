# Write a program to create a circular doubly linked list for an opened one,
#  such as l= None<-Head<=>1<=>2<=>3<=>4->None. By calling cirDul_LL(l), 
# you will get Head<=>1<=>2<=>3<=>4<=>Head. 
# The diagrams of doubly linked list and circular doubly linked list are shown as follows

class Node():
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList():
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if(self.head is None):
      self.head = newNode
      newNode.prev = self.head
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = newNode
    newNode.prev = current

  def showContents(self):
    contents = []
    current = self.head

    while current:
      contents.append(current.data)
      if(current.next is not self.head):
        current = current.next
      else:
        print(contents)
        return

def isLinkedListCircular(l):
  if(l is None or l.head is None):
    print("Please provide a valid doubly linked list to proceed.")
    return

  current = l.head
  while current:
    if(current.next is l.head):
      return True
    else:
      current = current.next
  return False

##
# code to convert doubly linked list to circular doubly linked list
##
def cirDul_LL(l):
  if (not(l) or l.head is None):
    print("Please provide a valid doubly linked list to convert to circular list")
    return
  if(l is isLinkedListCircular(l)):
    print("Given linked list is circular. Please provide a non-circular one to provide")
    return

  start = l.head
  last = l.head
  while last.next:
    last = last.next
  start.prev = last
  last.next  = start



doublyLinkedList1 = DoublyLinkedList()
doublyLinkedList1.append(1)
doublyLinkedList1.append(2)
doublyLinkedList1.append(3)
doublyLinkedList1.append(4)
doublyLinkedList1.append(5)

doublyLinkedList1.showContents()
print("Given doubly linked list is circular?", isLinkedListCircular(doublyLinkedList1))

# Converts the given non circular linked list to non-circular one
cirDul_LL(doublyLinkedList1)
doublyLinkedList1.showContents()
print("Given doubly linked list is circular?", isLinkedListCircular(doublyLinkedList1))
