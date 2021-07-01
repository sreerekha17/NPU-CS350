#Sorting a doubly linked list

def srt_LL(ll):
  if (not ll.head):
    return ll

  current = ll.head

  while current.next:
    next = current.next
    
    while next:
      if current.data > next.data:
        dataToReplace = current.data
        current.data = next.data
        next.data = dataToReplace
      
      next = next.next
    current = current.next

  return ll

class Node(object):
  """ A Doubly-linked lists' node. """
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """ Append an item to the list. """

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def iter(self):
        """ Iterate through the list. """
        current = self.head #note subtle change
        while current:
            val = current.data
            current = current.next
            yield val

    def print_foward(self):
        """ Print nodes in list from first node inserted to the last . """
        for node in self.iter():
            print(node)

    def showContents(self):
      curr = self.head
      items = []
      while curr:
        items.append(curr.data)
        curr = curr.next
      print(items)

dl1 = DoublyLinkedList()
dl1.append(4)
dl1.append(3)
dl1.append(2)
dl1.append(5)
dl1.append(1)
dl1.showContents()
dl1_sorted = srt_LL(dl1)
print("after sort")
dl1.showContents()
