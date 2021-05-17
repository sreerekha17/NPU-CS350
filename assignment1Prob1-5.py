import re
#################### Problem 1 #####
def fact_ls(m):
    return [k for k in range(1, m) if m% k == 0]

print(fact_ls(6))
print(fact_ls(8))
print(fact_ls(28))

#################### Problem 2 #####
def merge(lst1, lst2):
    mergedList = lst1 + lst2
    return sorted(mergedList)

print(merge([1, 3, 5], [2, 4, 6]))
print(merge([], [2, 4, 6]))
print(merge([1, 2, 3], []))
print(merge([5, 7], [2, 4, 6]))

############### Problem 3 ##########

def split_str(ls):
    vowels = 'a|e|i|o|u|\s+'
    # strAfterSplit = ls.split(vowels)
    strAfterSplit = re.split(vowels, ls, flags=re.IGNORECASE)

    return [s for s in strAfterSplit if s != '']

print(split_str('NPUoffersCS350inpythonlanguage'))

############### Problem 4 ############

def encryption(ls, map):
    # Solution 1: Looping through map and replacing characters in string
    encryptedString = ls
    for key, val in map.items():
        encryptedString = encryptedString.replace(key, map[key])
    return encryptedString

    #Solution 2:
    encrypted_str = ls
    for letter in encrypted_str:
        if (letter in map):
            print(letter, map[letter] )
            encrypted_str = encrypted_str.replace(letter, map[letter])
    return encrypted_str


testStr = 'data structure is very important for programming'
testMap = {
    'a': '1',
    'r': '2',
    'u': '3',
    'm': '4',
    ' ': '_'
}

print(encryption(testStr, testMap))


################ Problem 5 ####################
def square(x):
    return x * x

def two(x):
    return 2

def skp(f):
    #Complete
    def innerFunc():
        def deepInnerFunc(k):
            return f(k)
        return deepInnerFunc
    return innerFunc

def cmps(f, g):        #Complete statement
    def innerFunc (k):
        return f(g(k))
    return innerFunc

def add(f, g):          #Complete statement
    def innerFunc(k):
        return f(k) + g(k)
    return innerFunc

print("cmps()", cmps(square, two)(7))
print("cmps()", cmps(two, square)(2))
print("skp", skp(add(square, two))()(3))

