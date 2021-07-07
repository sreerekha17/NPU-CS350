##
# Check whether there exists random pointer in doubly linked list or not and correct it by a program, 
# as example as follows for function input and output
##

class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = newNode
      newNode.prev = curr

  def showContents(self):
    contents = []
    curr = self.head
    while curr:
      contents.append(curr.data)
      curr = curr.next
    print(contents)
    
def checkRandomPointer(list):
  if(list is None or list.head is None):
    print("Invalid list")
    return
  randomPointerExists = False
  if (list.head.prev is not None or list.head.next.prev != list.head):
    randomPointerExists = True
    return randomPointerExists
  curr = list.head.next
  while curr:
    if ((curr.next and curr.next.prev != curr) or (curr.prev and curr.prev.next != curr)):
      randomPointerExists = True
      return randomPointerExists
    curr = curr.next
  return False

def fixPointersInDL(list):
  if(list is None or list.head is None):
    print("Invalid list")
    return
  
  if(not(checkRandomPointer(list))):
    print("Doubly linked list is formed correctly. No action needed.")
    return

  if (list.head.prev is not None): ##prev of head node should point to None
    list.head.prev = None


  curr = list.head.next
  head = list.head
  print("prev, curr, next", curr.prev.data, curr.data, curr.next.data)
  if(curr.prev != head): #fixing the node after head to point prev to head
    curr.prev = head
  elif curr.prev.next != curr:
    curr.prev.next = curr
  while curr:
    print("prev, curr, next", curr.prev and curr.prev.data, curr.data,  curr.next and curr.next.data)
    if (curr.prev and curr.prev.next != curr):
      curr.prev.next = curr
      return
    
    elif (curr.next and curr.next.prev != curr): #when next node's prev not pointing to the current node
      curr.next.prev = curr
      return

    curr = curr.next


dl = DoublyLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.append(5)

dl.showContents()
print(checkRandomPointer(dl))    #returns False

dlWithRandomPointer = DoublyLinkedList()
dlWithRandomPointer.append(1)
dlWithRandomPointer.append(2)
dlWithRandomPointer.append(3)
dlWithRandomPointer.append(4)
dlWithRandomPointer.append(5)
dlWithRandomPointer.showContents()

# checking if a random pointer exists in a normal doubly linked list

print("Before making random pointer", checkRandomPointer(dlWithRandomPointer))    #returns False

# adding a pointer at third node to the next of next node

print("connecting", dlWithRandomPointer.head.next.data, dlWithRandomPointer.head.next.next.next.data ) #connects 2 to 4
dlWithRandomPointer.head.next = dlWithRandomPointer.head.next.next
print("After adding random pointer", checkRandomPointer(dlWithRandomPointer)) #returns True

fixPointersInDL(dlWithRandomPointer)
print("After fixing the pointers in DL", checkRandomPointer(dlWithRandomPointer)) #returns False
dlWithRandomPointer.showContents()

