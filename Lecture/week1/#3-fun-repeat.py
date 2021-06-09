#If "f" is a function taking in a positive integer n as only one argument, then we can implement the nth repeated calculating of "f", whose value at x in second order is f(f(...(f(x))). Following the examples shown in the def block, complete the foo function 

# def 	foo(f, n):
#    			    """Return the function that computes the nth repeated calculating of "f"
# incr(5)	#"incr", which is needed to create first, is to add # 1  for input argument number
#     6	
#     add_3 = foo (incr, 3) 
#     add_3 (5)        		# computing: incr(incr(incr(incr(incr(3)))))      
#     8
#     foo (triple, 5)(1)  		# triple(triple(triple(triple(triple(1)))))
#     243
#     foo (square, 2)(5) 		# square(square(5))
#     625
#     foo(square, 4)(5) 		# square(square(square(square(5))))
#     152587890625
#     			   """
# 			   """ Write your program here"""

def foo(f, n):
    def repeater(x, m=n):
        if (m ==1):
            return f(x)
        else:
            return f(repeater(x, m-1))
    return repeater

### test helpers ###
def incr(x):
    return x + 1
def triple(x):
    return 3*x
def square(x):
    return x * x


add_3 = foo(incr, 3)
print(add_3(5))           # => 8
print(foo(triple, 5)(1))  # => 243
print(foo(square, 2)(5))  # => 625
print(foo(square, 4)(5))  # => 152587890625
