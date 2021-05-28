# Given an integer, for example, "34567" has subsequences that include "345", "456", "346", "567" and so on, write the function max_seg to find the maximum subsequence below a certain length t.

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
    if (t < 1):
        return 0
    m = str(m)
    if(t > len(m)):
        ('0'*(t-len(m)))+str(m)

    def getSegment(n):
        if (n > 1):
            i = 0
            segs = []
            while i <= len(m) - n:
                j = i+1
                while j <= len(m) - (n-1):
                    segs.append(m[i]+m[j:j+(n-1)])
                    j += 1
                i += 1

            return segs + getSegment(n-1)
        else:
            return [k for k in m]

    allSegments = list(getSegment(t))
    allSegments = [int(k) for k in allSegments ]
    return max(allSegments)

print(max_seg(1254, 3)) #254
print(max_seg(1254, 4)) #1254
print(max_seg(1254, 5)) #1254 note that 1254 == 01254 
print(max_seg(1254, 2)) #54
print(max_seg(1254, 0)) # 0 is of length 0 => 0
print(max_seg(1254, 1)) #=>5 