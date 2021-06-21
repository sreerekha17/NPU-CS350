### Problem 3: Find minimum value and maximum value by functions/methods 
# for a given singly linked list with number or char type node value, 
# such as lst= head->3->1->2 
# ->NULL by calling a = min_num_linked_list(lst), a will be 1; if lst=head->C->A 
# ->B->NULL, and a = min_str_linked_list(lst), a is A. Likewise,
# the same principle is for getting max value,
# like max_num_linked_list(lst) and max_str_linked_list(lst)

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

def iterateLL(ll):
  current = ll.head
  while current:
    if current.data:
      val = current.data
      current = current.next
      yield val
##
# Solution 1: iterate over linked list and compare one by one
##
def min_num_linked_list(ll):
  min = None
  for data in iterateLL(ll):
    if min is None:
      min = data
    elif data < min:
      min = data
  return min

##
# Solution 2: iterate over linked list, store as array 
# and use the min/max method to get the smallest and largest
##

def min_num_linked_list_solution2(ll):
  contents = getContentsAsArray(ll)
  return min(contents)

def max_num_linked_list(ll):
  max = None
  for data in iterateLL(ll):
    if max is None:
      max = data
    elif data > max:
      max = data
  return max

def min_str_linked_list(ll):
  min = None
  for data in iterateLL(ll):
    if min is None:
      min = data
    elif data < min:
      min = data
  return min

def max_str_linked_list(ll):
  max = None
  for data in iterateLL(ll):
    if max is None:
      max = data
    elif data > max:
      max = data
  return max

lst = SinglyLinkedList()
lst.append(3)
lst.append(1)
lst.append(2)

print("list 1 contents", getContentsAsArray(lst), " Smallest is ", min_num_linked_list(lst), " and largest is ", max_num_linked_list(lst))

lst2 = SinglyLinkedList()
lst2.append('C')
lst2.append('A')
lst2.append('B')
print("list 2 contents", getContentsAsArray(lst2), " Smallest is ", min_str_linked_list(lst2), " and largest is", max_str_linked_list(lst2))
