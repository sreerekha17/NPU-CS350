#Problem 4: In an algebraic expression, 
# such as "x – (y + z)", generate a function/method based on stack operations 
# to rewrite it without parenthesis, like "x – y – z", ONLY considering + and – operators 
# in this expression. If an expression is "x – (y – z – (u+v) ) – w", 
# the new format should be "x – y + z + u + v  – w" after function/method call 


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
      if( not self.isEmpty()):
        return self.items[len(self.items) -1]
      else:
        return None
    def display(self):
      contents = ''
      while len(self.items):
        contents += self.items.pop()
      print(contents)
    
    def size(self):
      return len(self.items)

def evaluateExpression(exp):
  if not exp or exp == '':
    print("Empty expression is provided.")
    return

  print(exp)
  operands = Stack()
  result = ''

  changeOperand = None
  for i in exp:
    if i == '(':
      if not operands.isEmpty():
        changeOperand = operands.peek()
      else:
        changeOperand = None #nothing to change if bracket is in the beginning
      i == ''
    
    elif changeOperand is not None:
      if i == '–' and changeOperand == '–':
        i = '+'
      elif i == '+' and changeOperand == '–':
        i = '–'
      elif i == '-' and changeOperand == '+':
        i = '–'
      elif i == ')':
        i = ''
      result += i
      operands.push(i)
    
    elif (i == '–' or i == '+'):
      operands.push(i)
      result += i
    elif i == ')':
      changeOperand = None
    else:
      result += i

  print(result)






exp1 = 'x – ( y + z )'
evaluateExpression(exp1)  #x - y - z

exp2 = 'x – ( y – z – ( u + v ) ) – w' # x - y + z + u + v - w
evaluateExpression(exp2)