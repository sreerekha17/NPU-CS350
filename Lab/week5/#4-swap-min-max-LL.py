# Problem 4: Write a program to swap positions of min and max node value 
# in a given singly linked list.
# For instance, s1= head->3->1->2->NULL, the new one will be 
# head->1->3->2->NULL through swap_num_linked_list(s1);
# following the same rule for char node value, it is like s2= head->C->A->B->NULL, 
# calling swap_char_linked_list(s2) will get head->A ->C ->B->NULL

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      current = self.head
      while current and current.next:
        current = current.next
      current.next = newNode
  
def getContentsAsArray (ll):
  current = ll.head
  items = []
  while current:
    if (current.data):
      items.append(current.data)
    current = current.next
  return items

def swap_num_linked_list(ll):
  contents = getContentsAsArray(ll)
  minVal = min(contents)
  maxVal = max(contents)
  print("min, max", minVal, maxVal)

  current = ll.head
  while current:
    if (current.data == minVal):
      current.data = maxVal
    elif (current.data == maxVal):
      current.data = minVal
    current = current.next

list1 = SinglyLinkedList()
list1.append(3)
list1.append(1)
list1.append(2)

print("Before swap", getContentsAsArray(list1))
swap_num_linked_list(list1)
print("After swap", getContentsAsArray(list1))

list2 = SinglyLinkedList()
list2.append('C')
list2.append('A')
list2.append('B')

print("Before Swap", getContentsAsArray(list2))
swap_num_linked_list(list2)
print("After Swap", getContentsAsArray(list2))

list2 = SinglyLinkedList()
list2.append('C')
list2.append('C')
list2.append('C')

print("Before Swap", getContentsAsArray(list2))
swap_num_linked_list(list2)
print("After Swap", getContentsAsArray(list2))
