# 5. (Bonus) Given a positive number N, 
# 2*N elements from 1 to N can be created in a list, 
# such as N=3, and list will be 1, 1, 2, 2, 3, 3 
# with two appearances of 1s, 2s and 3s. 
# Write a program to find all sequences between its two appearances 
# with required distance, which is exactly equal to value of the element. 
# For instance, the following two sequences meet the requirements:

# 	e.g.		3 1 2 1 3 2	
# 		            3 … …3		# 3 elements in between	
# 			  1… 1             		# 1 element in between
# 			     2……2      		# 2 elements in between

# 	e.g.		2 3 1 2 1 3	
#                         2……2      		# 2 elements in between
# 		               3 … …3		# 3 elements in between	
# 			     1… 1           	# 1 element in between

# 	If N = 4, two sequences will be 

# 			4 1 3 1 2 4 3 2		
# 			4 … …   4 		# 4 elements in between
# 			  1… 1           		# 1 element in between
# 			     3 … …3		# 3 elements in between
# 				2……2		# 2 elements in between

# 			2 3 4 2 1 3 1 4
# 			2……2			# 2 elements in between
# 			   3 … …3		# 3 elements in between
# 			      4 … …   4 		# 4 elements in between
# 			          1… 1           	# 1 element in between

def getSequenceWithDistance(numbers, start, n):
  # TODO yet to implement
  return 


def sequenceGenerator(n):
  if n < 3:
    print('required sequence cannot be generated with n < 3')
    return
  
  numbers = [None] * 2 * n
  start = 1
  getSequenceWithDistance(numbers, start, n)




sequenceGenerator(3)
