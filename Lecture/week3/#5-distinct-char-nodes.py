##
# Write a function diffElem_LL(l, m) as similar as above,
# but to exact all char values, which are NOT common ones,
# and link them together, such as 
# "Head->D->o->g->L->E->NULL",   
##
class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
  
  def append(self, data):
    newNode = Node(data)
    if (not(self.head)):
      self.head = newNode
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = newNode

def iterate(ll):
  curr = ll.head
  while curr:
    val = curr.data
    curr = curr.next
    yield val

def showContents(ll):
  if (not(ll) or not(ll.head)):
    return
  else:
    contents = []
    curr = ll.head
    while curr:
      contents.append(curr.data)
      curr = curr.next

    print("contents", contents)
    return contents

def dataChecker(ll, data):
  if(not(ll) or not(ll.head)):
    return False
  curr = ll.head
  while curr:
    if (curr.data == data):
      return True
    curr = curr.next
  return False

def diffElem_LL(l, m):
  distinct = []
  for letter in iterate(l):
    if( not (dataChecker(m, letter))):
      distinct.append(letter)
  
  for i in iterate(m):
    if(not(dataChecker(l, i))):
      distinct.append(i)

  distinctLL = SinglyLinkedList()
  for char in distinct:
    distinctLL.append(char)
  return distinctLL


l = SinglyLinkedList()
l.append('G')
l.append('O')
l.append('O')
l.append('D')
      
m = SinglyLinkedList()
m.append('G')
m.append('o')
m.append('O')
m.append('g')
m.append('L')
m.append('E')

distinctDataList = diffElem_LL(l, m)
print("distinct elements", showContents(diffElem_LL(l, m)))