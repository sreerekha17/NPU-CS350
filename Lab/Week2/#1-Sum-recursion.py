#########  Problem 1 #########
# Complete sum function in recursion with two arguments, a positive integer m and a function func. It applies func to every number from 1 to m including m and returns the sum of the results.

# def sum(m, func):

#     """Return the sum of the first m terms in the sequence defined by func.
#     Implement using recursion!

#     sum(5, lambda x: x * x * x) 	# 1^3 + 2^3 + 3^3 + 4^3 + 5^3
#     225
#     sum (9, lambda x: x + 1) 	# 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
#     54
#     sum (5, lambda x: 2**x) 		# 2^1 + 2^2 + 2^3 + 2^4 + 2^5
#     62
    
#     # Do NOT use while/for loops!
#     """
#     assert  n >= 1

#     """ Write your program here"""

def Sum(m, func):
    if (m == 1):
        return func(m)
    else:
        return func(m) + Sum(m-1, func)

print(Sum(5, lambda x: x * x * x)) #     225
print(Sum(9, lambda x: x + 1))     #     54
print(Sum(5, lambda x: 2**x))      #     62