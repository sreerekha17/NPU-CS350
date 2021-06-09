# Problem #2: The bounce-back-forth sequence is a serial number from 1 and is always either counting up or counting down. In kth number, the direction changes when k is divisible by 7 or contains the digit 7. The first 30 elements of the bounce-back-forth sequence are listed below, with direction change marked in RED color at the 7th, 14th, 17th, 21st, 27th, and 28th elements: 

# Index sequence in the serial:  1 2 3 4 5  6   7   8 9 10 11 12 13 14 15 16 17 18 19 20 21  22 23 24 25 26 27  28  29 30
# bounce-back-forth sequence: 1 2 3 4 5 6 [7] 6 5 4   3  2  1 [0] 1  2 [3] 2  1  0 [-1] 0  1   2  3  4  [5] [4] 5  6 

# Write a function bounce-back-forth that returns the kth element of the bounce-back-forth sequence. 


# def 	bnc_bck_frth(k): 

#  			 """Return the kth element of the bounce-back-forth sequence. 
#   bnc_bck_frth (7) 
#    7 
#   bnc_bck_frth (8) 
#   6 
#   bnc_bck_frth (15) 
#   1 
#   bnc_bck_frth (21) 
#  -1 
#   bnc_bck_frth (22) 
#   0 
#   bnc_bck_frth (30) 
#   6
# 	  bnc_bck_frth (68) 
#   2 
#   bnc_bck_frth (69) 
#   1 
#   bnc_bck_frth (70) 
#   0 
#   bnc_bck_frth (71) 
#   1 
#   bnc_bck_frth (72) 
#   0 
#   bnc_bck_frth (100) 
#  	  2 
# 			"""
# 			""" Write your program here"""

def isIndexDeterminingNumber(n):
    if n > 10:
        return n % 10 == 7 or n %7 == 0 or isIndexDeterminingNumber(n//10)
    elif n < 10:
        return n == 7
    else:
        return False

def bnc_bck_frth(k):
    determining_indices = [0]
    for i in range(1, k +1):
        if (isIndexDeterminingNumber(i)):
            determining_indices.append(i)

    if(determining_indices[len(determining_indices) -1] != k):
        determining_indices += [k]

    nextOperation = '+'
    index = 0
    for j in range(1, len(determining_indices)):
        i = j-1
        if (nextOperation == '-'):
            index -= determining_indices[j] - determining_indices[i]
            nextOperation = '+'
        else:
            index += determining_indices[j] - determining_indices[i]
            nextOperation = '-'
    return index

print(bnc_bck_frth(7))   # => 7
print(bnc_bck_frth(8))   # => 6
print(bnc_bck_frth(15))  # => 1
print(bnc_bck_frth(21))  # => -1
print(bnc_bck_frth(22))  # => 0
print(bnc_bck_frth(30))  # => 6
print(bnc_bck_frth(68))  # => 2
print(bnc_bck_frth(69))  # => 1
print(bnc_bck_frth(70))  # => 0
print(bnc_bck_frth(71))  # => 1
print(bnc_bck_frth(72))  # => 0
print(bnc_bck_frth(100)) # => 2




    
