# Assuming that the following special list structure generation functions, like is_Slist(s) and Slist(first, rest) have been defined and the output is a list-of-list, write a function flat to change list-of-list to single layer list structure.

# empty = []

# def is_Slist(s):
#   return s == empty or (len(s) == 2 and is_Slist(s[1]))

# def Slist(first, rest):
#   assert is_Slist(rest),    "rest must be a Slist list."
#   return [first, rest]

# lst = Slist(12, Slist(99, Slist(37, [] )))
# lst
# [12, [99, [37, []]]]

# lst2 = Slist(1, Slist(2, Slist(3, (4, []))))
# lst2
# [1, [2, [3, (4, [])]]]

# 		#---------------------------------------
# def 	flat(ls):
#    			    """
#     print(flat(lst))
#     [12, 99, 37]	

#     print(flat(lst2))
#     [1, 2, 3, 4]
# 		   """
# 		   """ Write your program here"""


empty = []
def is_Slist(s):
    return s == empty or (len(s == 2) and is_Slist(s[1]))

def Slist(first, rest):
    return [first, rest]

lst = Slist(12, Slist(99, Slist(37, [])))    # [12, [99, [37, []]]]
# print("lst", lst)

lst2= Slist(1, Slist(2, Slist(3, (4, []))))  # [1, [2, [3, (4, [])]]]
# print("lst2", lst2)

def flat(ls):      #complete flat method
    if (len(ls) > 1 and ls[1] != empty):
        return [ls[0]] + flat(ls[1][0:])
    else:
        return [ls[0]]
    

print(flat(lst)) # [12, [99, [37, []]]] => [12, 99, 37]
print(flat(lst2)) # [1, [2, [3, (4, [])]]] => [1, 2, 3, 4]
