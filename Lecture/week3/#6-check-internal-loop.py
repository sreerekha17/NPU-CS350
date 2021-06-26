## Problem 6: 
# Given a linked list, write a program to 
# check if there exists an internal linked loop or not. 
# For instance, as following, 
# return value of function/method is_loopLL(a) is true, otherwise false.
##


class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.count = 0
  
  def append(self, data):
    newNode = Node(data)
    if (not(self.head)):
      self.head = newNode
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = newNode
    self.count += 1

def connectAtGivenPos(ll, pos):
  end = ll.head
  currentPos = 1
  connector = ll.head
  while pos != currentPos:
    connector = connector.next
    currentPos += 1
  while end.next:
    pos += 1
    end = end.next
  end.next = connector

##
# returns True if the node has a loop
##
def checkIfGivenListIsLoop(ll):
  if(not(ll) or not(ll.head)):
    return False
  
  previousNodes = []

  curr = ll.head
  while curr:
    if (curr in previousNodes):
      return True
    
    previousNodes.append(curr)
    curr = curr.next
  return False

ll1 = SinglyLinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)

##
# creates a new loop from the last node to the 3rd node
##

connectAtGivenPos(ll1, 3)

# ll1 is now a looped list


print("ll1 has a loop ->", checkIfGivenListIsLoop(ll1))

#creates Another list with no loop
ll2 = SinglyLinkedList()
ll2.append(10)
ll2.append(20)
ll2.append(30)
ll2.append(40)
ll2.append(50)

print(f"ll2 is a loop ->", checkIfGivenListIsLoop(ll2))
