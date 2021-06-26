##
# Problem 2: Assuming that there are two linked lists with positive number type value in each node,
# such as u= "Head->1->2->3->4->NULL" and v="Head->5->6->7->8->NULL", 
# two numbers 1234 & 5678 from the linked lists can be extracted respectively, 
# and make addition operation for two numbers, the result will be 6912(=1234+5678) .
# Find a function/method to implement above operations and get such result "Head->6->9->1
#	->2->NULL" if calling function LL_add(u,v)  
##
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.count = 0

  def append(self, data):
    newNode = Node(data)
    if (self.head is None):
      self.head = newNode
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode

def showContents(ll):
  if (not(ll) or not(ll.head)):
    return

  current = ll.head
  contents = []
  
  while current:
    contents.append(current.data)
    current = current.next
  return contents

def getTotalDataInList(ls):
  if (not(ls) or not(ls.head)):
    return 0
  current = ls.head
  total = 0
  while current:
    if (current.next):
      power = len(str(current.data))
      total = (total*10**power + current.data *10**power)
    else:
      total = (total + current.data)
    current = current.next
  return total

def newLLFromAddition(list1, list2):
  total = getTotalDataInList(list1) + getTotalDataInList(list2)
  print(total)
  newList = SinglyLinkedList()
  if (total > 0):
    num = total
    def addByRecursive(n):
      if (n > 0):
        addByRecursive(n//10)
        newList.append(n%10)
    addByRecursive(num)
  return newList

list1 = SinglyLinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)

list2 = SinglyLinkedList()
list2.append(5)
list2.append(6)
list2.append(7)
list2.append(8)

newList = newLLFromAddition(list1, list2)
print(showContents(newList))  # 1234 + 5678 = 6912; head -> 6 -> 9 -> 1 -> 2

##
# creates two lists head -> 1 -> 2 and head -> 3 -> 4
##
list3 = SinglyLinkedList()
list3.append(1)
list3.append(2)
list4 = SinglyLinkedList()
list4.append(3)
list4.append(4)


newList = newLLFromAddition(list3, list4)
print(showContents(newList)) # 12 + 13 = 46; head -> 4 -> 6