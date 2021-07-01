import numpy as np

class Node:
  def __init__(self, data, idx):
    self.data=data
    self.idx=idx
elm0=Node("head",1)
elm1=Node("S",2)
elm2=Node("t",3)
elm3=Node("i",4)
elm4=Node("n",5)
elm5=Node("g",None)


ls=np.array([elm0,elm1,elm2,elm3,elm4,elm5])

def rev(ls):
  if(not(len(ls))):
    return
  newLs = np.array([])
  newLs = np.array([Node("head", ls[-2].idx)]) #gets the last data and index
  for i in range(-2, -len(ls)-1):
    #incomplete, idea is to get the current data, and add the index of previous one from the previous to previous' index 
    node = Node(ls[i].data, ls[i-2].idx)
    np.append(newLs, [node])

  print(newLs[0].data )
print(ls[2].data)


len(ls)
rev(ls)



