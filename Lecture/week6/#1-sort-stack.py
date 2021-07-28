#Problem 1: Write a function/method to sort char type elements in stack by 
# ONLY temporary stack (shown in the example programs) 
# or one variable without using list. For example, given a stack stk,
# the result should be as follows after calling srt(stk) 


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

def sortStack(stack):
  if (isEmptyStack(stack)):
    print("Given stack is empty")
    return

  sortedStack = createStack()

  while stackSize(stack):
    temp = last(stack)
    popitem(stack)
    
    while(stackSize(sortedStack) and last(sortedStack) > temp):
      push(stack, last(sortedStack))
      popitem(sortedStack)

    push(sortedStack, temp)
      
  return sortedStack


stk = createStack()
push(stk, 't')
push(stk, 'r')
push(stk, 'o')
push(stk, 's')


print(sortStack(stk))