# 3. Given an array with positive integer elements, 
# such as arr = {1, 3, 2, 1, 2, 1}, 
# write a program to partition it to two subsets (arrays) with equal sum of all elements,
# like ls1={1, 1, 1, 2} and ls2 = {2, 3}, having sum 5 in each array.
# Notice that the solution may NOT be unique, such as ls1={3, 1, 1} and ls2 = {2, 2, 1}
# are other two subsets to meet requirements as well

def getPossibleMaxSum(arr):
  possibleMaxSum = 0
  for i in arr:
    possibleMaxSum += i
  
  return int(possibleMaxSum/2)
  

def partitionToSubsets(arr):
  if not arr or not len(arr):
    print("Empty array")
    return
  
  possibleMaxSum = getPossibleMaxSum(arr)  
  print("possibleMaxSum", possibleMaxSum)

  subset_1 = []
  total_1 = 0
  subset_2 = []
  total_2 = 0

   #for second subset, reading backwards
  for i in range(-1, -len(arr), -1):
    if (total_2 + arr[i] < possibleMaxSum):
      total_2 += arr[i]
      subset_2.append(arr[i])
    elif total_2 + arr[i] == possibleMaxSum:
      total_2 += arr[i]
      subset_2.append(arr[i])

  #for first subset, reading forward
  for i in range(0, len(arr)):
    if(total_1 + arr[i] < total_2):
      total_1 += arr[i]
      subset_1.append(arr[i])
    elif total_1 + arr[i] == total_2:
      total_1 += arr[i]
      subset_1.append(arr[i])
  
  print("subsets are", subset_1, subset_2)



arr = [1, 3, 2, 1, 2, 1]
partitionToSubsets(arr)


arr2 = [12,13, 10, 1, 2, 1]
partitionToSubsets(arr2)


#todo try another possible implementation by coverting the array to a circular linked list, and see if the total matches