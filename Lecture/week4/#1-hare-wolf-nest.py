# 1. In an open farmland where a hare (similar as rabbit) lives, it usually sleeps in any suitable place, continually shifting from one place to another in total 10 nests labeled from 1 to 10.
# But a wolf lives in the same area, hunting to check 10 nests in the manner as follows: 

# start to check from label 1 nest
# then skip one nest (label 2) to check label 3
# increase skipped checking number to 2 (skip label 4 and label 5) and look for it in label 6
# keep increasing skipped number to 3 to check label 10
# go back to count from label 1 by increasing skipped number to 4 and so on

# Write a program to help this hare to make a decision which nests are safe to sleep, maybe doesn't exist at all after the wolf checked n times

# 	Hint: create a circular linked list and traverse one by one circularly.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularList:
  def __init__(self):
    self.head = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if (self.head is None):
      self.head = newNode
    else:
      curr = self.head
      while curr.next and curr.next is not self.head:
        curr = curr.next
      curr.next = newNode
    newNode.next = self.head

def findSafeNest(ll, n):
  if(n <= 1):
    print("Please provide a higher n value to proceed")
    exit()
  count = 1
  curr = ll.head
  step = 0
  safe = [i for i in range(1, 11)]
  safe.remove(curr.data)
  while count <= n:
    for i in range(1, step+2):
      curr = curr.next
    curr = curr.next
    
    print("removes data", curr.data, step)
    if(len(safe) and curr.data in safe):
      safe.remove(curr.data)
    step += 1
    if(curr.next is ll.head): #assumes one loop completed when approaching head, and increments count
      count += 1

  print("safe nests are", safe)

cl = CircularList()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.append(5)
cl.append(6)
cl.append(7)
cl.append(8)
cl.append(9)
cl.append(10)

findSafeNest(cl, 5)

findSafeNest(cl, 25)