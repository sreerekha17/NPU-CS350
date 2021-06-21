### Problem 2: 
# Create a function/method to concatenate two singly linked lists, like 
# ls1= head->4->2->1-> NULL, and ls2= head->5->7->3-> NULL. 
# From function/method call concat_linked_list(ls1, ls2), 
# the result is head->4->2->1->5
# ->7->3->NULL

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
    if self.head is None:
      self.head = newNode
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
    
    self.count +=1
  
def displayContents(ls):
  current = ls.head
  contentsArr = []
  while current:
    if (current.data):
      contentsArr.append(current.data)
    current = current.next
  print("contentsArr", contentsArr)

def concat_linked_list(ls1, ls2):
  if ls1.head is None and ls2.head is None:
    return ls1
  
  elif ls1.head is None:
    ls1.head = ls2.head
    return ls1
  
  endOfList1 = ls1.head
  while endOfList1.next:
    endOfList1 = endOfList1.next
  
  endOfList1.next = ls2.head
  return ls1

list1 = SinglyLinkedList()
list1.append(4)
list1.append(2)
list1.append(1)

list2 = SinglyLinkedList()
list2.append(5)
list2.append(7)
list2.append(3)

displayContents(list1)
displayContents(list2)

emptyLS = SinglyLinkedList()

print("After concat of two non empty LL" )
displayContents(concat_linked_list(list1, list2))

print("After concat of one non-empty and one empty list")
displayContents(concat_linked_list(list1, emptyLS))

print("After concat of one empty and one non-empty list")
displayContents(concat_linked_list(emptyLS, list1))

print("After concat of two empty list")
emptyLS1 = SinglyLinkedList()
displayContents(concat_linked_list(emptyLS1, emptyLS1))