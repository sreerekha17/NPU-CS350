###
# 5. From given a linked list with integer value nodes, 
# calculate average value, for instance, input linked list a = "Head->1->2->3->NULL". 
# By calling function or a method in a class, Average_List(a), average value is (1+2+3) / 3=2.0 
# (floating data type).
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
  def append(self, new_data= None):
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
  
  ###-----------------------------------------------------------------###
  # SOLUTION TO PROBLEM : find the average of all nodes in a data #
  # but keep the first occurrence itself                                #
  ###-----------------------------------------------------------------###

  def avg_list(self):
    if(not(self.head)):
      return 0

    current = self.head
    total = 0
    count = 0
    while current:
      if (isinstance(current.data, int) or isinstance(current.data, float)): #checks for data is an int or float
        total += current.data
      count += 1
      current = current.next
    
    return total/count


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

print("original linked list is", a.display(), " and its average is ", a.avg_list())

##
# creates a linked list with all nodes with same data
##
b = linked_list()
b.append(3)
b.append(3)
b.append(3)
b.append(3)
print("original list is", b.display(), " and its average is ", b.avg_list())

##
# creates an empty linked list
##
c = linked_list()
print("original list is", c.display(), " and its average is ", c.avg_list())

##
# creates list with few nodes with no data
##
d = linked_list()
d.append(3)
d.append()
d.append(10)
d.append()
d.append(4)
print("original list is", d.display(), " and its average is ", d.avg_list())
