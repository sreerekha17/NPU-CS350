class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

class CircularList():
  def __init__(self, n):
    if(n<=0):
      print("Please enter a higher n value to create matrix")
      return
    self.head = Node(1)
    prev = self.head
    for i in range(2, n+1):
      prev.next = Node(i)
      prev = prev.next
    prev.next = self.head

  def showContents(self):
    curr = self.head
    while curr:
      print(curr.data)
      if not(curr.next is self.head):
        curr = curr.next
      else:
        return

def createMatrix(ls, n):
  if(n<=0):
    print("Please enter a higher n value to create matrix")
    return
  result = []
  count = 1
  start = ls.head
  while count <= n:
    row = []
    i = 1
    while i <=n:
      row.append(start.data)
      i += 1
      start = start.next
    
    start = start.next
    count += 1
    result.append(row)
  print(result)



n3 = CircularList(3)
n3.showContents()
createMatrix(n3, 3)

n4 = CircularList(4)
n4.showContents() 
createMatrix(n4, 4)

n0 = CircularList(0)
