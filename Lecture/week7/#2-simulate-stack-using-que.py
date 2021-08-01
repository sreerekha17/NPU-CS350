# 2.   Create a function to simulate stack push & pop 
# operations by using only ONE queue
from collections import deque

class Stack():
    def __init__(self):
        self.items = deque()
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if len(self.items):
            self.items.pop()
        else:
            print("Empty Stack")
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        if len(self.items):
            return False
        else:
            return True

stk1 = Stack()
print("isEmpty", stk1.isEmpty())
stk1.push(1)
stk1.push(2)
stk1.push(3)
stk1.push(4)
stk1.push(5)

print("After adding", stk1.items)
stk1.pop()

print(stk1.items)
