##
# Problem 3: Solve monkey king election question on the handout 
# by circular linked list in a program
# 	Input 
# 		Enter total number of monkeys in a group: 5 
# 		Enter m value: 3 

#       Output 
# 		The king will be 3 

#       Input 
# 		Enter total number of monkeys in a group: 8 
# 		Enter m value: 5 

#      Output 
# 		The king will be 2 

# Notice that 1st monkey’s label should start with 0 as an index 


class Node():
  def __init__(self, data):
    self.data = data
    self.next = None


class CircularLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if (self.head):
      self.head.next = newNode
      self.head = newNode
    else:
      self.head = newNode
      self.tail = newNode
    self.head.next = self.tail
    self.count += 1

def showContents(cll):
  if( not(cll) or not(cll.tail)):
    return
  else:
    items = []
    curr = cll.tail
    count = 1
    while count <= cll.count:
      items.append(curr.data)
      curr = curr.next
      count += 1
    return items


def getMonkeyKing(n, m):
  monkeyLs = CircularLinkedList()
  for i in range(0, n):
    monkeyLs.append(i)
  print("monkey list", showContents(monkeyLs))
  prev = monkeyLs.tail
  curr = monkeyLs.tail

  while monkeyLs.count > 1:
    count = 1
    while count < m:
      prev = curr
      curr = curr.next
      count += 1
    prev.next = curr.next
    curr = prev.next
    monkeyLs.count -= 1

  return curr.data

king = getMonkeyKing(5, 3)
print("Monkey king when 5 monkeys and m = 3 is", king)

king = getMonkeyKing(8, 5)
print("Monkey king when 8 monkeys and m = 8 is", king)

