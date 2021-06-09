###
# 3. Create a program to delete all duplicated elements in a linked list, 
# such as a = "Head->1->2->1->3->2->NULL". 
# After calling function or a method in a class, Delete_Dupl_Node(a), 
# the new linked list will be "Head->1->2->3->NULL".
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
  
  def length(self):
    if not(self.head):
      return 0
    cur=self.head
    total=0
    while cur:
        total+=1
        cur=cur.next
    return total
  
  def display(self):
    elems=[]
    cur_node=self.head
    while cur_node:
        elems.append(cur_node.data)
        cur_node=cur_node.next
    return elems
  
  ###-----------------------------------------------------------------###
  # SOLUTION TO PROBLEM : custom method to remove duplicate occurrences #
  # but keep the first occurrence itself                                #
  ###-----------------------------------------------------------------###
  def keepUniqueList(self):
    currentNode = self.head
    prevNode = self.head
    dataList = []
    while currentNode:
      if (currentNode.data in dataList):
          prevNode.next = currentNode.next
      else:
        dataList.append(currentNode.data)
        prevNode = currentNode
      currentNode = currentNode.next

      
        
# creating a linked list with few random nodes with duplicate data
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

print("original list data", a.display())
a.keepUniqueList() # removed duplicates
print("after removing all duplicates", a.display())

##
# creates a linked list with all nodes with same data
##
b = linked_list()
b.append(3)
b.append(3)
b.append(3)
b.append(3)
print("original list is", b.display())
b.keepUniqueList()
print("after removing all duplicates", b.display())

##
# creates an empty linked list
##
c = linked_list()
c.keepUniqueList()
print("length of list after removing all duplicates", c.display())

