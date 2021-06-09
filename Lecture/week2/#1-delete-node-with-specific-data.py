# Problem #1. Write a program to delete all elements in a given linked list with the value same as input argument key,
# such as input linked list a = "Head->1->2->1->3->NULL". 
# After calling function or a method in a class, Delete_LinkList_Node (a, 1), 
# the new linked list will be "Head->2->3->NULL".

# 	Hint: take example programs as reference


## Creating Node and linked list referenced from example source code
# Singly Linked List
class Node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

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
  # SOLUTION TO PROBLEM : custom method to remove a node with specific datas #
  # but keep the first occurrence itself                                     #
  ###----------------------------------------------------------------------###
  def delete_linkedList_node(self, val):
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

##
#  creating a linked list with few nodes
##
mixed_list = linked_list()
mixed_list.append(1)
mixed_list.append(1)
mixed_list.append(3)
mixed_list.append(5)
mixed_list.append(1)
mixed_list.append(4)
mixed_list.append(1)
mixed_list.append(9)
print("original list is", mixed_list.display())

mixed_list.delete_linkedList_node(1)
print("linked list after removing nodes with data as 1 is", mixed_list.display())

###
# creates a new linked list with all nodes with same value and removes the same
##
allSevenLinkedList = linked_list()
allSevenLinkedList.append(7)
allSevenLinkedList.append(7)
allSevenLinkedList.append(7)
allSevenLinkedList.append(7)
allSevenLinkedList.append(7)

print("original all 7 linked list", allSevenLinkedList.display())
#remove 7 from linked list
allSevenLinkedList.delete_linkedList_node(7)
print("llinked list after removing 7 is", allSevenLinkedList.display())

emptyList = linked_list()
emptyList.delete_linkedList_node(7)
print("empty linked list after removing us", emptyList.display())

linkedListWithEmptyNode = linked_list()
print("original Linked list with empty nodes", linkedListWithEmptyNode)
linkedListWithEmptyNode.append(3)
linkedListWithEmptyNode.append(None)
allSevenLinkedList.delete_linkedList_node(None)

print("linked list after removing us", linkedListWithEmptyNode.display())
