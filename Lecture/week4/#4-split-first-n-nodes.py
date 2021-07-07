# 4. Find a program to split from first N nodes into new circular linked list with int type nodes 
# while preserving the old nodes. For instance, org = Head->2->3->4->5->6->7->8
# 	->Head, two new circular linked lists should be Head->2->3->4->Head and 
# 	Head->5->6->7->8->Head from the outputs of function call split_CLL(org, 3)


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def append(self, data):
    newNode = Node(data)
    if(self.head is None):
      self.head = newNode

    else:
      curr = self.head
      while curr.next is not self.head:
        curr = curr.next
      curr.next = newNode
    newNode.next = self.head
    self.count += 1
  
  def showContents(self):
    if(self.head is None):
      return
    data = []
    curr = self.head
    data.append(curr.data)
    curr = curr.next
    while curr is not self.head:
      data.append(curr.data)
      curr = curr.next
    print(data)

def split_CLL(orig, n):
  if (orig.head is None or n < 1):
    print("Please provide a valid linked list and higher n greater than 1 to proceed")
    return

  count = 1
  current = orig.head
  firstHalf = CircularLinkedList()
  secondHalf = CircularLinkedList()
  totalLength = orig.count
  if( n > totalLength):
    print("Please provide a valid n value corresponding to the length of list")
    return
  while count <= n:
    firstHalf.append(current.data)
    current = current.next
    count += 1
  
  while count < totalLength:
    secondHalf.append(current.data)
    current = current.next
    count += 1
  
  print("first half")
  firstHalf.showContents()
  print("second half")
  secondHalf.showContents()
  return (firstHalf, secondHalf)

orig = CircularLinkedList()
orig.append(2)
orig.append(3)
orig.append(4)
orig.append(5)
orig.append(6)
orig.append(7)
orig.append(8)

split_CLL(orig, 7)