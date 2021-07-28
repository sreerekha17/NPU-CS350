#Problem 3: Given a stack saving a group of int type values from the bottom to the top, 
# find whether or not there exist pair values in consecutive sequence for all elements 
# by a program and print these pairs. For instance, two stacks are as follows

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

def consecutiveSequenceChecker(s):
    temp = []
    while (len(s) != 0):
        temp.append(s[-1])
        s.pop()
    result = True
    while (len(temp) > 1):
      first = temp[-1]
      temp.pop()
      next = temp[-1]
      temp.pop()
      if (abs(first - next) != 1):
          result = False
          print("Unmatched pair is", first, next )
      else:
        print("Pair is", first, next )
      s.append(first)
      s.append(next)
 
    if (len(temp) == 1):
        s.append(temp[-1])
 
    return result

stk = createStack()

push(stk, 4)
push(stk, 5)
push(stk, -2)
push(stk, -3)
push(stk, 11)
push(stk, 10)
push(stk, 5)
push(stk, 6)
push(stk, 20)
print(consecutiveSequenceChecker(stk)) #returns True

stk1 = createStack()

push(stk1, 4)
push(stk1, 6)
push(stk1, 6)
push(stk1, 7)
push(stk1, 4)
push(stk1, 3)

print(consecutiveSequenceChecker(stk1))



