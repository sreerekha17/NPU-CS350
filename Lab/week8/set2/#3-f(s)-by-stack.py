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
        return 0
    def display(self):
      contents = ''
      while len(self.items):
        contents += self.items.pop()
      print(contents)
    
    def size(self):
      return len(self.items)

integersAdded = Stack()
storedFValues = Stack()

def findFnew(n):
    fPrev = storedFValues.peek() or 0

    fNew = max(fPrev, 0) + n
    storedFValues.push(fNew)

    return fNew

print(findFnew(1))
print(findFnew(2))
print(findFnew(-2))
print(findFnew(4))
print(findFnew(5))