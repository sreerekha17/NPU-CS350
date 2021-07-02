# Implement node sequence reversion in doubly linked list with char type value through a rev(ls) function call. Assume that original list is like 
# None<-Head<=>a<=>b<=>c<=>d<=>e->None, the result should be 
# None<-Head<=>e<=>d<=>c<=>b<=>a->None after function call
# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def append(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode
      newNode.prev = temp

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

  def rev(self):
    curr = self.head
    while curr:
      hold = curr.prev
      curr.prev = curr.next
      curr.next = hold
      curr = curr.prev
    self.head = hold.prev

ls = LinkedList()
ls.append('a')
ls.append('b')
ls.append('c')
ls.append('d')
ls.append('e')
ls.PrintList()
ls.rev()
print("after reverse")
ls.PrintList()