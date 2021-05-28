#Problem 2: Given an integer, for example, "34567" has subsequences that include "345", "456", "346", "567" and so on, write the function max_seg to find the maximum subsequence below a certain length t.

# def max_seg(m, t):

# """Return the max subsequence of length at most t that can be found in the given number m.

#     For example, for m = 1254 and t =3, we have that the subsequences are
#         	1
# 	2
# 	5
# 	4
# 	12
# 	15
# 	14
# 	25
# 	24
# 	54
# 	125
# 	245

#     and of these, the max number is 245, so the answer is 245.

#     max_seg(1254, 3)
#     245
#     max_seg(1254, 4)
#     1254
#     max_seg(1254, 5) 		# note that 1254 == 01254
#     1254
#     max_seg (1254, 2)
#     25
#     max_seg(1254, 0) 		# 0 is of length 0
#     0
#     max_seg(1254, 1)
#     5
# """
#     """ Write your program here"""


def max_seg(m, t):
    def getCombinations(m, t):
        def getSegments(n, u, s):
            if (n > 0):
                return [(n%10**(u-1))*10 + s] + getSegments(n//10, u, s) + getSegments(n//10, u, n%10)
            else:
                return [s]
        if(t >= 1):
            return (getSegments(m//10, t, m%10) + getCombinations(m, t-1))
        else:
            return [0]
    return max(getCombinations(m, t))

print(max_seg(1254, 3))  #254
print(max_seg(1254, 4))  #1254
print(max_seg(1254, 5))  #1254 note that 1254 == 01254 
print(max_seg(1254, 3))  #54
print(max_seg(1254, 0))  # 0 is of length 0 => 0
print(max_seg(1254, 1))  #=>5 
print(max_seg(19516, 3)) #956
print(max_seg(34567, 3)) #567
