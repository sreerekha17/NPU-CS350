# Being similar as above question, 
# delete all elements by a value in a char type node linear list-array after the function call,
# and re-organize the rest elements in CONSECUTIVE index. For instance, 
# ls: {'b', 'e', 'e', 'e', 'a', 't', 'e', 'r'}, the result should be ls: {'b', 'a', 't', 'r'} 
# and length is 4 in the new list from function call deleteElem(ls, 'e')

def deleteElem(ls, val):
  if not ls or not len(ls) or not val:
    print("Invalid list or data provided.")
    return
  updated = []
  
  for i in ls:
    if i != val:
      updated.append(i)
  
  return updated

arr = ['b', 'e', 'e', 'e', 'a', 't', 'e', 'r']

print(deleteElem(arr, 'e'))