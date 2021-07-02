# Given a list of list(i.e. nested list), such as ls = [1, [2, [3,4]], [[5, 6], 7]] , write a function/method flatten(ls) to create singly linked list Head ->1->2->3->4->5->6->7
# ->None

class Node:
  def __init__(self, data):
    self.data = data  # Assign data
    self.next = None  # Initialize next as null

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, new_data):

    # 1. Create a new node
    # 2. Put in the data
    # 3. Set next as None
    new_node = Node(new_data)

    # 4. If the Linked List is empty, then make the
    #    new node as head
    if self.head is None:
        self.head = new_node
        return

    # 5. Else traverse till the last node
    last = self.head
    while (last.next):
        last = last.next

    # 6. Change the next of last node
    last.next =  new_node
    
  def printData(self):
    curr = self.head
    items = []
    while curr:
      items.append(curr.data)
      curr = curr.next
    print(items)

# def flatten(ls):
#   if not(len(ls)):
#     return LinkedList()
#   newList = LinkedList()

#   node = ls
#   while node:
#     print(node, node[0])
#     newList.append(node[0])
#     node = node[1]

#   newList.printData()

empty = []
# def is_Slist(s):
#     return s == empty or (len(s == 2) and is_Slist(s[1]))

# def Slist(first, rest):
#     return [first, rest]

# lst = Slist(12, Slist(99, Slist(37, [])))    # [12, [99, [37, []]]]
# # print("lst", lst)

# lst2= Slist(1, Slist(2, Slist(3, (4, []))))  # [1, [2, [3, (4, [])]]]
# # print("lst2", lst2)

# def flatten(ls):
#   if (len(ls) > 1 and ls[1] != empty and len(ls)):
#       return [ls[0]] + flatten(ls[1][0:])
#   else:
#       return [ls[0]]

def flatten(ls):
    contents = []
    for i in ls:
      if type(i) == list:
          for j in flatten(i):
              contents.append(j)
      else:
          contents.append(i)
    return contents

def LLfromList(l):
  newList = LinkedList()
  for i in l:
    newList.append(i)
  return newList

ls = [1, [2, [3,4]], [[5, 6], 7]]
flat_contents = flatten(ls)
newLs = LLfromList(flat_contents)
newLs.printData()
