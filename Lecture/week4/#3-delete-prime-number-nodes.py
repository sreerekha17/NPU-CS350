#3. Given a circular linked list with int type value at each node, 
# write a program to delete all  prime number nodes, 
# such as m= Head->13->12->15->14->Head, after calling delete_prime_CLL(m),
# you will get Head->12->15->14->Head

def isPrimeNumber(n):
  if (n <=1 ):
    return False
  if n == 2:
    return True
    
  primeNumber = True
  divisor = 2
  while divisor <= n/2:
    if n%divisor == 0:
      primeNumber = False
      return False
    else:
      divisor += 1
  return primeNumber

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

  def append(self, data):
    newNode = Node(data)
    if(self.head is None):
      self.head = newNode

    else:
      curr = self.head
      while curr.next is not self.head:
        curr = curr.next
      curr.next = newNode
    newNode.next = self.head
    self.count += 1
  def showContents(self):
    if(self.head is None):
      return
    data = []
    curr = self.head
    data.append(curr.data)
    curr = curr.next
    while curr is not self.head:
      data.append(curr.data)
      curr = curr.next
    print(data)

def getLastNode(m):
  lastNode = m.head
  while lastNode.next is not m.head:
    lastNode = lastNode.next
  return lastNode

def delete_prime_CLL(m):
  if (m.head is None):
    print("Empty list provided")
    return
  curr = m.head
  last = getLastNode(m)

  count = 0
  while count < m.count:
    if isPrimeNumber(curr.data):
      if curr is m.head:
        m.head = curr.next
        last.next = m.head
      else:
        last.next = curr.next
      
    else:
      last = curr
    curr = curr.next
    count += 1

#
# Linked list with prime in head and tail
#
clWithPrime = CircularLinkedList()
clWithPrime.append(3)
clWithPrime.append(5)
clWithPrime.append(7)
clWithPrime.append(9)
clWithPrime.append(11)
clWithPrime.append(49)
clWithPrime.append(53)
clWithPrime.showContents()

delete_prime_CLL(clWithPrime)

clWithPrime.showContents()

##
# Linked list with prime on head
##
m = CircularLinkedList()
m.append(13)
m.append(12)
m.append(15)
m.append(14)
m.showContents()
delete_prime_CLL(m)
print("After removing prime numbers -")
m.showContents()

##
# empty Linked list
##
n = CircularLinkedList()
n.showContents()
delete_prime_CLL(n)
print("After removing prime numbers -")
n.showContents()

##
# adding non prime numbers to the ll
##
n.append(10)
n.append(12)
n.append(14)
n.append(16)
n.showContents()
delete_prime_CLL(n)
print("After removing prime numbers -")
n.showContents()