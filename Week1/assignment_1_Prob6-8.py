from operator import add
############### Problem 6 #########################

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

m = lambda h: h(2)   #def fun(h) => return h(2)

print("h(m)", h(m))