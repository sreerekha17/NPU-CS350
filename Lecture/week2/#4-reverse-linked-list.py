###
# 4. Write a program to reverse the element sequence for given linked list, 
# like a = "Head->1->2->3->NULL". 
# Through calling function or a method in a class, Reverse_Node(a), 
# the new linked list will be "Head->3->2->1->NULL".
### 

## Creating Node and linked list referenced from example source code
# Singly Linked List
from typing import Reversible


class Node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

def isDuplicate(list, val):
  if (not(list) or not(list.data) ):
    return False
  else:
    current = list
    while current:
      if (current.data == val):
        return True
      else:
        current = current.next

class linked_list:
  def __init__(self):
    self.head = None

# Adds new node containing 'data' to the end of the linked list.
  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return
    
    last = self.head
    while (last.next):
      last = last.next
    
    last.next = new_node
  
  def display(self):
    elems=[]
    cur_node=self.head
    while cur_node:
      elems.append(cur_node.data)
      cur_node=cur_node.next
    return elems

  ###----------------------------------------------------------------------###
  #                                                                          #
  # SOLUTION TO PROBLEM : custom method reverse given linked list            # 
  ###----------------------------------------------------------------------###
  def reverse(self):
    if(not(self.head) or not(self.head.next)):
      return self.head

    current = self.head.next
    prev = Node(self.head.data)
    
    while current:
      nextCurr = current.next
      current.next = prev
      prev = current
      current = nextCurr
    self.head = prev


# creating a linked list with few nodes
a = linked_list()
a.append(1)
a.append(3)
a.append(5)
a.append(1)
a.append(4)
a.append(8)
a.append(8)
a.append(1)
a.append(9)
a.append(4)

##
# creates a linked list with mixed data
##
print("original linked list is", a.display())


a.reverse()
print("list after reverse", a.display())

##
# creates a linked list with all nodes with same data
##
b = linked_list()
b.append(3)
b.append(3)
b.append(3)
b.append(3)
print("original b is", b.display())
b.reverse()
print("list after reverse", b.display())

##
# creates an empty linked list
##
c = linked_list()
c.reverse()
print("list after reverse", c.display())

