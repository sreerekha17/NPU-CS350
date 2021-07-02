# Given a singly linked list with char type nodes from a-zA-Z, like 
# ls = Head->c->o->m->m->i->t->t->e->e->None, write a program to delete 
# ALL nodes if the consecutive values are the same. After del(ls) function call,
#  Head->c->o->i->None will be the return value

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
    
# def del_ll(ll):
#   if not(ll.head):
#     return
  
#   current = ll.head
#   prev = ll.head
#   while current:
#     if(current.next):
#       if(current.data == current.next.data):
#         print(current.data)
#         if(current.next.next):
#           prev.next = current.next.next
#         else:
#           prev.next = None
#     prev = current
#     current = current.next

def del_ll(ll):
  if not(ll.head):
    return
  
  current = ll.head
  prev = ll.head
  while current:
    if(current.next):
      if(current.data == current.next.data):
        print(current.data)
        if(current.next.next):
          prev.next = current.next.next
          current = prev.next
        else:
          prev.next = None
          current = None
      else:
        prev = current
        current = current.next

ll = LinkedList()
ll.append('c')
ll.append('o')
ll.append('m')
ll.append('m')
ll.append('i')
ll.append('t')
ll.append('t')
ll.append('e')
ll.append('e')
ll.printData()
del_ll(ll)
ll.printData()