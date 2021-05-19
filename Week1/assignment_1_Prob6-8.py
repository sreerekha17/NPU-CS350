############### Problem 6 #########################

from operator import add
from math import sqrt

def curry(h):
    def innerFunc(x):
        def deepInner(y):
            return h(x, y)
        return deepInner
    return innerFunc


five = curry(add)(3)(2)
print(five)

############### Problem 7 #########################

def h(m):
    h = m

    def m(h):
        return h
    return h(m)

m = lambda h: h(2)
h(m)

print("h(m)", h(m))

############# Problem 8 ##############################
### Check whether the number given is a prime number or not using recursion 

def is_prime(n):
    numberIsPrime = True
    initialDivisor = 2
    def checkPrime(divisor, n_sqrt):
        if (divisor <= n_sqrt and n%divisor == 0):
            return False
        elif (divisor <= n_sqrt and n%divisor != 0):
            return checkPrime(divisor+1, n_sqrt)
        else:
            return True

    if (n <= 1):
        numberIsPrime = False
    elif (n==2):
        numberIsPrime = True
    else:
        n_sqrt = sqrt(n)
        numberIsPrime = checkPrime(initialDivisor, n_sqrt)
    
    if (numberIsPrime):
        result = "Given number {} is a Prime Number"
    else:
        result = "Given number {} is NOT a Prime Number"
    print(result.format(n))
    return numberIsPrime

is_prime(-4)
is_prime(4)
is_prime(7)
is_prime(47)
is_prime(23)