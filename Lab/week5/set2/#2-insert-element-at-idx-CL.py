
# Create a function/method to insert an element by index to circular linked list.
#  After that, verify it by several test cases. For instance, given circular linked list 
# ls = Head->1->2->3->4->Head, after calling function cirLL_insert (ls, 1, 123), 
# the new one will be Head->1->123->2->3->4->Head

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList():
  def __init__(self):
    self.head = None

  def append(self, data):
    newNode = Node(data)

    if self.head is None:
      self.head = newNode
    else:
      curr = self.head
      while curr:
        if(curr.next is self.head):
          curr.next = newNode
        else:
          curr = curr.next
    newNode.next = self.head

  def showContents(self):
    if (not(self.head)):
      return
    contents = []

    curr = self.head
    print("head is", curr.data)
    while curr:
      contents.append(curr.data)
      if (curr.next is not self.head):
        curr = curr.next
      else:
        print("contents are", contents)
        return
    
  def getEndNode(self):
    if(not self or self is None):
      return None
    else:
      endNode = self.head
      while endNode.next != self.head:
        endNode = endNode.next
      return endNode

  def cirLL_insert(self, pos = 1, data=None):
    if (not(self) or not(self.head) or data is None):
      print("Pass required data")
      exit()
    
    currPos = 0
    currentNode = self.head
    prevNode = self.head
    newNode = Node(data)
    endNode = self.getEndNode()
    while currentNode:
      if (pos == currPos):
        if (pos == 0): #insert at head, then replace the current head with new head
          self.head = newNode
          newNode.next = currentNode
          endNode.next = self.head
        else:
          prevNode.next = newNode
          newNode.next = currentNode
        return
      else:
        if (currentNode.next is not self.head):
          prevNode = currentNode
          currentNode = currentNode.next
        else:
          print("Given index is not valid")
          exit()
      currPos += 1

cl1 = CircularLinkedList()
cl1.append(1)
cl1.append(2)
cl1.append(3)
cl1.append(4)
cl1.append(5)
cl1.showContents()

#Inserting 123 at index 1
cl1.cirLL_insert(1, 123)
cl1.showContents()

#Inserting 0 at index 0
cl1.cirLL_insert(0, 0)
cl1.showContents()


#Inserting 444 at index 4
cl1.cirLL_insert(4, 444)
cl1.showContents()

#Trying to insert at a larger index
cl1.cirLL_insert(8, 222)
cl1.showContents()




