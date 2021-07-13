# Write a program to create new list with the common char type values from two lists-array
# by using linear list structure-array, 
# such as la: {'C', 'o', 'm', 'p', 'l', 'i', 'm', 'e', 'n', 't'}, 
# and     lb: {'c', 'o', 'm', 'p', 'l', 'e', 'm', 'e', 'n', 't'},  you will get 
#         lc: {     'o', 'm', 'p', 'l',      'm', 'e', 'n', 't'} 
# through function call cmmSq(la, lb)

def cmmSq(la, lb):
  if not la or not len(la) or not lb or not len(lb):
    print("Both list must cannot be empty")
    return

  common = []
  for i in range(0, len(la)):
    if la[i] == lb[i]:
      common.append(la[i])
  print(common)
  return common

list1 = ['C', 'o', 'm', 'p', 'l', 'i', 'm', 'e', 'n', 't']
list2 = ['c', 'o', 'm', 'p', 'l', 'e', 'm', 'e', 'n', 't']

cmmSq(list1, list2)

