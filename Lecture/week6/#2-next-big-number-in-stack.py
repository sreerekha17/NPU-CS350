# Assuming that there is a series of int type values in stack, such as 
# stck ->"5 3 2 10 6 8 1 4 12 7 4", write a program to get next bigger value 
# for each element ONLY using stack allowed operations,
# like 5->10,  3->10, 2->10, 10->12, 6->8, 8->12, 1->4, 4->12, 12->none, 7->none, 4->none
 
from collections import deque

def createStack():
  stack = []
  return stack

def isEmptyStack(stack):
  return not stack or len(stack) == 0

def stackSize(stack):
  return len(stack)

def last(stack):
  length = len(stack)
  return stack[length-1]

def popitem(stack):
  if(isEmptyStack( stack )):
    print("Empty stack")
    return

  return stack.pop()

def push( stack, item ):
    stack.append( item )


# def getNextBiggestNumber(stack):
#   i = 0
#   while i < len(stack):
#     k = stack.index(i)
#     print(i)
#     i += 1
 
 
def getNextBiggestNumber(L):
  n = len(L)
  s = []

  temp = [None for i in range(n)]
  for i in range(n - 1, -1, -1):
      while (len(s) > 0 and s[-1] <= L[i]):
          s.pop()

      if (len(s) == 0):
          temp[i] = None      
      else:
          temp[i] = s[-1]    

      s.append(L[i])
     
  for i in range(n):
    print(L[i], " -> ", temp[i] )

stk = deque()
stk.append(5)
stk.append(3)
stk.append(2)
stk.append(10)
stk.append(6)
stk.append(8)
stk.append(1)
stk.append(4)
stk.append(12)
stk.append(7)
stk.append(4)

print(getNextBiggestNumber(stk))

