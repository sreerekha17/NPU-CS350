class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, new_data):

    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while (last.next):
        last = last.next

    last.next =  new_node

  def printList(self):
    contents = []
    temp = self.head
    while (temp):
      contents.append(temp.data)
      temp = temp.next
    print(contents)

def getLength(ls):
  curr = ls.head
  count = 0
  while curr:
    curr = curr.next
    count += 1
  print(count)
  return count

def getReversedList(items):
  ls = LinkedList()
  for i in range(-1, -len(items)-1, -1):
    print("reversed list", items[i])
    ls.append(items[i])
  return ls

def sep(ls):
  if not(ls) or ls.head is None:
    print("Please provide a non empty linked list to split")
    return
  
  lenOfList = getLength(ls)

  firstHalfContents = []

  ls2 = LinkedList()

  current = ls.head

  if (lenOfList %2 == 0): #even number of nodes
    print("is even")
    count = 0
    while count < lenOfList/2:
      firstHalfContents.append(current.data)
      current = current.next
      count += 1
    
    print("firstHalfContents", firstHalfContents)
    ls1 = getReversedList(firstHalfContents)
  
    #second half
    while current:
      ls2.append(current.data)
      current = current.next
    ls1.printList()
    ls2.printList()
  else:
    print("odd list - skip the middle one")
    count = 0
    while count < lenOfList/2 - 1:
      firstHalfContents.append(current.data)
      current = current.next
      count += 1
    
    print("firstHalfContents", firstHalfContents)
    ls1 = getReversedList(firstHalfContents)

    current = current.next

    #second half
    while current:
      ls2.append(current.data)
      current = current.next
    ls1.printList()
    ls2.printList()

  
ls = LinkedList()
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.append(5)
ls.append(6)

getLength(ls)
sep(ls)

ls_odd = LinkedList()
ls_odd.append(10)
ls_odd.append(20)
ls_odd.append(30)
ls_odd.append(40)
ls_odd.append(50)
ls_odd.append(60)
ls_odd.append(70)
getLength(ls_odd)
sep(ls_odd) 