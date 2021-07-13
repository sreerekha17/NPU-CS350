# Assuming that all int type values are saved in an array,
#  like a = {3, 9, 10, 1, 30, 40},
#  find a function to get maximum value from a[u] – a[v] + a[w] –a[x],
#  where indices must be u>v>w>x. (40-1+10-3) will be the result based on given array


testArr = [3, 9, 10, 1, 30, 40]

def getMin(arr):
  return min(arr)

def getMax(arr):
  return max(arr)

#finds and returns the max for a[u] – a[v] + a[w] –a[x]
#  u- largest,
#  w- second largest,
#  v- smallest,
#  x- second smallest

def getMaxValForGivenFormula(arr):
  if not arr or len(arr) < 4:
    print("Array must have atleast 4 elements to proceed")
    return

  largest = getMax(arr[3:])
  u = 0
  for i in range(0, len(arr)):
    if(arr[i] == largest):
      u = i
  
  smallest = getMin(arr[2:u])
  v = 0
  for i in range(0, len(arr)):
    if(arr[i] == smallest):
      v = i

  secondLargest = getMax(arr[1:v+1])
  w = 0
  for i in range(0, len(arr)):
    if(arr[i] == secondLargest):
      w = i

  secondSmallest = getMin(arr[0:w])
  x = 0
  for i in range(0, len(arr)):
    if(arr[i] == secondSmallest):
      x = i
  
  print("u =", u, "v =", v, "w =", w, "x =", x)
  print("arr[u] =", arr[u], "arr[v] =", arr[v], "arr[w]=", arr[w], "arr[x]=", arr[x])

  output = arr[u] - arr[v] + arr[w] - arr[x]
  print("output of formula is", output)
  return output

getMaxValForGivenFormula(testArr)