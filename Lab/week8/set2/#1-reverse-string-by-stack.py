# Problem 1: Given a char array with initial value, like string = "reward",
# write a program to reverse array by stack after calling rev(string), 
# and return value will be 
# newString = "drawer"

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

def rev(string):
    if not string or string == '':
        print("Empty string")
        return

    stk = Stack()

    for i in string:
        stk.push(i)
    
    i = 0
    reversed = ''
    while i < stk.size():
        reversed += stk.pop()
    return reversed



testString1 = "reward"
print(testString1, "after reverse ->", rev((testString1)))
