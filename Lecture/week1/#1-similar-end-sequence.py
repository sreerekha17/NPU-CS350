
# Write a def function with only one positive integer argument in recursion to 
# find a sequence of number, which always ends up with … 4, 2, 1 ☺ in terms of the following number processing,
#  and after that, please verify it by test cases as shown below. Notice that do NOT make n value too big. 
# Otherwise, it might take very long time (i.e. one of big disadvantages in recursive function) for the computing system to calculate 

# If n is even, divide it by 2
# If n is odd, multiply it by 3 and add 1
# Continue this process until n is 1

# Test cases: 
# n=3; 10, 5, 16, 8, 4, 2, 1
#  n=4; 2, 1
#  n=5; 16, 8, 4, 2, 1
#  n=6; 3, 10, 5, 16, 8, 4, 2, 1
#  n=7; 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

def endInSameSequence(n):
    def sequenceGenerator(m):
        if (m ==1):
            return [1]
        else:
            return [m] + sequenceGenerator(m/2) if m%2 ==0 else [m] + sequenceGenerator(m*3+1)

    sequence = sequenceGenerator(n)
    return sequence[1:]

print(endInSameSequence(3))
print(endInSameSequence(4))
print(endInSameSequence(5))
print(endInSameSequence(6))
print(endInSameSequence(7))
print(endInSameSequence(17))
print(endInSameSequence(11))
