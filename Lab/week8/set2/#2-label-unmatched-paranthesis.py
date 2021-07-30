# Create a program to label unmatched parentheses in an expression from keyboard read-in. 
# Assuming that the expression consists of only parentheses and upper/lower case English alphabet from A-Z/a-z, 
# if unmatched left-half parentheses is found, label it by "$" and  unmatched right-half parentheses by "?" as the following examples

# 	Inputs from keyboard: 
# Enter an expression like:  ((ABCD(x)

# 	Outputs:
# 		Unmatched parentheses:  $$


# 	Inputs from keyboard: 
# Enter an expression like:  )(rttyy())sss)(

# 	Outputs:
# 		Unmatched parentheses: ?                ?$


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



#Alternate solution without using stack

def labelUnmatchedSecondApproach(string):
    if not string or string == '':
        print("String is empty")
        return

    paranthesisMapping = {
        '(': '$',
        ')': '?'
    }

    openingBrackets = []
    pattern = ''
    for i in range(0, len(string)):
        if string[i] == '(':
            openingBrackets.append(i)
            pattern += ' '
        elif string[i] == ')':
            if len(openingBrackets):
                openingBrackets.pop() #remove the last opening bracket as the closing one satisfies
                pattern += ' '
            else:
                pattern += paranthesisMapping[')']
        
        else:
            pattern += ' '

    for i in range(0, len(pattern)):
        if i in openingBrackets:
            pattern = pattern[:i] + paranthesisMapping['('] + pattern[i + 1:]

    return pattern

testStr = '((ABCD(x)'
print(labelUnmatchedSecondApproach(testStr))

testStr2 = ')(rttyy())sss)('
print(labelUnmatchedSecondApproach(testStr2))

#Solution 2 - Uses stack, but does not add spaces as the above solution
def labelUnmatched(string):
    if not string or string == '':
        print("String is empty")
        return

    paranthesisMapping = {
        '(': '$',
        ')': '?'
    }

    leftSet = '('
    rightSet = ')'

    lTracker = Stack()
    rTracker = Stack()

    pattern = ''
    for i in string:
        if i == leftSet:
            lTracker.push(i)
        elif i == rightSet:
            if lTracker.size():
                lTracker.pop()
            else:
                pattern += paranthesisMapping[rightSet]
                rTracker.push(i)
            
    for i in range(0, lTracker.size()):
        pattern += paranthesisMapping[leftSet]
    
    return pattern

