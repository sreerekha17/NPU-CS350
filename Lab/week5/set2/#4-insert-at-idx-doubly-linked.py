# Generate a function/method to insert an element by index to doubly linked list. 
# If existing list is like lst= None<-Head<=>1<=>2<=>3<=>4->None,
#  the result should be None<-Head<=>1<=>123<=>2<=>3<=>4->None through 
# 		dul_LL_insert (lst, 1, 123) function/method call



class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList():
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if (self.head is None):
      self.head = newNode
      newNode.prev = self.head
      return

    current = self.head
    while current.next:
      current = current.next
    
    current.next = newNode
    newNode.prev = current

  def insertAtIndex(self, pos, data):
    newNode = Node(data)
    if(pos == 0):
      curr = self.head
      self.head = newNode
      newNode.prev = curr.prev
      newNode.next = curr.next
      return
    
    currentPos = 0
    current = self.head
    prev = self.head

    while current:
      if (pos == currentPos):
        prev.next = newNode
        newNode.prev = prev
        newNode.next = current
        current.prev = newNode
        return
      else:
        prev = current
        current = current.next
        currentPos += 1
    print("Index is invalid. Please provide a valid index to continue.")

  def showContents(self):
    if(not self.head):
      return

    contents = []
    current = self.head
    while current:
      contents.append(current.data)
      current = current.next
    print(contents)

cl1 = DoublyLinkedList()
cl1.append(1)
cl1.append(2)
cl1.append(3)
cl1.append(4)
cl1.append(5)
cl1.showContents()
cl1.insertAtIndex(0, 0)
cl1.showContents()

cl1.insertAtIndex(2, 222)
cl1.showContents()

cl1.insertAtIndex(5, 555)
cl1.showContents()
