###
# 2. Find a program to delete all duplicated value elements including itself in a linked list, 
# such as a = "Head->1->2->1->3->2->NULL". 
# After calling function or a method in a class, such as Delete_Node_value(a), 
# the new linked list will be "Head->3->NULL".
###


## Creating Node and linked list referenced from example source code
# Singly Linked List
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
  # SOLUTION TO PROBLEM : custom method to remove duplicate occurrences      # 
  # including itself                                                         #
  # but keep the first occurrence itself                                     #
  ###----------------------------------------------------------------------###
  def delete_node_value(self):
    currentNode = self.head
    while currentNode:
      if (isDuplicate(currentNode.next, currentNode.data)):
        self.removeDataWithGivenVal(currentNode.data)
      currentNode = currentNode.next

  def removeDataWithGivenVal(self, val):
    if (not(self.head)):
      print("Linked list is empty. Please add a non-empty linked list to proceed.")
    else:
      prevNode = self.head
      currentNode = self.head
      while (currentNode):
        if (currentNode.data == val):
          if (prevNode.data == val):
            self.head = currentNode.next
            prevNode = currentNode.next
          else:
            prevNode.next = currentNode.next
        else:
          prevNode = currentNode
        currentNode = currentNode.next


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


a.delete_node_value()
print("list after removing all duplicates", a.display())

##
# creates a linked list with all nodes with same data
##
b = linked_list()
b.append(3)
b.append(3)
b.append(3)
b.append(3)
print("original b is", b.display())
b.delete_node_value()
print("list after removing all duplicates", b.display())

##
# creates an empty linked list
##
c = linked_list()
c.delete_node_value()
print("list after removing all duplicates", c.display())

