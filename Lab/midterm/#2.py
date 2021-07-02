#In the singly circular linked list of an unsigned int type value node, such as 
# ls = Head->8->9->10->11->12->13->Head, create a function/method mov(ls) to move Head to prime number node, the new list should be like Head->11->12->13->8->9->10
# ->Head

#

def numIsPrime(n):
  isPrime = True
  if n > 1:
    for i in range(2, int(n/2)+1):
      if (n % i) == 0:
        isPrime = False
        break
    else:
        isPrime = True
 
  else: 
    isPrime = False
  return isPrime

def getPrimeNumberInCL(ll):
  primeFound = False
  for n in ll.iter():
    if numIsPrime(n):
      primeFound = True
      primeNumber = n
      break
  return primeNumber

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1
    
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    def printItems(self):
        curr = self.tail
        items = []
        while curr:
          items.append(curr.data)
        print(items)

    def mov(self):
      primeNumber = getPrimeNumberInCL(self)
      if(not(primeNumber)):
        print("No prime number in the given list, linked list unchanged")
        return self
      
      # previousHead = self.head
      curr = self.head
      prev = self.head
      while curr:
        if(curr.data == primeNumber):
          self.head = curr
          prev.next = self.head
          return
        else:
          prev = curr
          curr = curr.next 
          

      
ll = CircularList()
ll.append(8)
ll.append(9)
ll.append(10)
ll.append(11)
ll.append(12)
ll.append(13)
ll.printItems()

    
# primeNumber = getPrimeNumberInCL(ll)
# print(primeNumber)



