###
## Problem 1: Write a program to insert an element to singly linked list in terms of reverse index, 
# such as given a=head->11->12->13-> NULL, after calling function/method insert_rev_index(a, 1, 123),
#  and then new linked list will be 
## head->11->12->123->13-> NULL. And if calling insert_rev_index(a, 0, 456), 
# the new one should be head->11->12->123->13-> 456->NULL
###
class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
    self.count += 1
  
def insertAtPositionReverse(ll, pos, data):
  if pos > ll.count or pos < 0:
    print("Pls provide a valid position in range")
    return
  
  pos = ll.count - pos
  newNode = Node(data)
  current = ll.head
  currentPosition = 1
  
  while current:
    if (currentPosition == pos):
      if current == ll.head:
        newNode.next = ll.head
        ll.head = newNode
      else:
        newNode.next = current.next
        current.next = newNode
      ll.count += 1
      return
    else:
      currentPosition += 1
      current = current.next
      

def displayContents(ll):
  current = ll.head
  items = []
  while current:
    items.append(current.data)
    current = current.next
  print(items)


list1 = SinglyLinkedList()
list1.append(11)
list1.append(12)
list1.append(13)
print("Original list")
displayContents(list1)
insertAtPositionReverse(list1, 1, 123)
print("After inserting data 123 at position 1")
displayContents(list1)

print("After inserting data 456 at position 0")
insertAtPositionReverse(list1, 0, 456)
displayContents(list1)

print("After inserting data 333 at position 3")
insertAtPositionReverse(list1, 3, 333)
displayContents(list1)





