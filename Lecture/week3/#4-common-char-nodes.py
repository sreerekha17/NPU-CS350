##
# Given two singly linked lists with char type value node, like a-zA-Z
# l= "Head->G->O->O->D->NULL", and m ="Head->G->o->O->g->L->E->NULL",
#  Find the common char values and form a new linked list "Head->G->O->NULL" through a function/method called commElem(l, m). 
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

def commElem(l, m):
  if (not(l) or not(m) or not(l.head) or not(m.head)):
    return None
  else:
    lContents = []
    common = []
    for letter in iterate(l):
      lContents.append(letter)
    for letter in iterate(m):
      if (letter in lContents and not(letter in common)):
        common.append(letter)
    print("commonn letter", common)
    finalLL = SinglyLinkedList()
    for letter in common:
      finalLL.append(letter)

  return finalLL





l = SinglyLinkedList()
l.append('G')
l.append('O')
l.append('O')
l.append('D')
      
m = SinglyLinkedList()
m.append('G')
m.append('o')
m.append('O')
m.append('G')
m.append('L')
m.append('E')

print("common elements", showContents(commElem(l, m)))