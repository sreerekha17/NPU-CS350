# 1.	Through array structure, 
# find a function/method to get all element’s indices 
# and total number of duplicate elements for a certain value 
# in linear list-array with a char type node, such as given list 
# ls: {'b', 'e', 'e', 'e', 'a', 't', 'e', 'r'},
# after calling function getIndex (ls, 'e'),
# return indices like 1, 2, 3, 6 and total 4 'e's


def getIndex(ls, val):
  if not ls or not len(ls) or not val:
    print("Invalid list or data provided.")
    return
  indices = []
  for i in range(0, len(ls)):
    if ls[i] == val:
      indices.append(i)
  
  if(len(indices)):
    return indices, len(indices)
  else:
    print("Given value could not be found in the given list")

arr = ['b', 'e', 'e', 'e', 'a', 't', 'e', 'r']

print(getIndex(arr, 'e'))