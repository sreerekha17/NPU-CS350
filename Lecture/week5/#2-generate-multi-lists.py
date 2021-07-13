# Problem 2. Given a linked list with int type node ONLY from 0 to 9, like 
# 	lst0 = Head->1->2->2->1->None, and then other three lists can be generated after combinations of any two CONSECUTIVE nodes, such as lst1 = Head->12->2->1
# 	->None, lst2 = Head->1->22->1->None, and lst3 = Head->1->2->21->None. Please generate a function/method to convert those 4 lists to char type node linked list based on corresponding English letter 1 to 'A', 2 to 'B', … … 26 to 'Z'. If the number is bigger than 26, replace it with '#' character. So outputs will be Head->A->B->B->A->None from 
# 	Head->1->2->2->1->None, Head->L->B->A->None from Head->12->2->1
# 	->None, Head->A->V->A->None from Head->1->22->1->None, and Head->A->B
# 	->U->None from Head->1->2->21->None


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = newNode

  def showContents(self):
    curr = self.head
    contents = []
    while curr:
      contents.append(curr.data)
      curr = curr.next
    print(contents)

def joinNode(curr, next):
  return curr * 10 + next
  
def getListLength(ls):
  if not ls.head:
    return 0
  curr = ls.head
  length = 0
  while curr:
    length += 1
    curr = curr.next
  return length

def replaceContents(ls):
  if not ls or not ls.head:
    print("Cannot convert empty list")
    return
  
  mapWords = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
  }

  curr = ls.head

  while curr:
    if(curr.data in mapWords):
      curr.data = mapWords[curr.data]
    else:
      curr.data = '#'
    curr = curr.next
    
def makeNewLists(ls):
  if not ls or ls.head is None:
    print("Linked list is empty")
    return
  lengthOfList = getListLength(ls)
  
  pos = 1
  lists = []
  while pos < lengthOfList:
    count = 1
    newSubList = SinglyLinkedList()
    curr = ls.head
    while curr:
      if(pos == count):
        if curr.next:
          newNodeData = joinNode(curr.data, curr.next.data)
          newSubList.append(newNodeData)
          curr = curr.next.next
      else:
        newSubList.append(curr.data)
        curr = curr.next
      count += 1
    pos += 1
    lists.append(newSubList)
  lists.append(ls)

  print("Generated lists are:")
  for i in lists:
    i.showContents()
    replaceContents(i)
    i.showContents()

  return lists

testlist = SinglyLinkedList()
testlist.append(1)
testlist.append(2)
testlist.append(3)
testlist.append(4)
testlist.append(5)

testlist.showContents()
makeNewLists(testlist)

testlist1 = SinglyLinkedList()
testlist1.append(1)
testlist1.append(2)
testlist1.append(2)
testlist1.append(1)
testlist1.showContents()
makeNewLists(testlist1)