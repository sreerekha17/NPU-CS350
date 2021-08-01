# Write a function/method with positive int type argument, 
# such as genBin(7), and outputs will be binary number sequence from 
# to , like 11071012, 102, 112,1002by using queue structure, 1012, 1102, 111

from collections import deque
 
binQ = deque()

def generateBinary(n):
    return bin(n)[2:]

def genBin(n):
    if n < 1:
        print("Please enter a higher n value to proceed")
        return
    
    for i in range(1, n+1):
        n_bin =  generateBinary(i)
        binQ.append(n_bin)
    
    for i in range(0, n):
        print(binQ.popleft())

genBin((7))
