# Create a function pth(t, n) to find path from the root of the given tree (e.g. t) to node n, and returns a list data type, where the sequence of all elements in the list is each node's value along the path in the tree. If n is not present in tree, return None. Assuming that each node of the tree is unique, for the following tree, [7, 3, 6, 5] will be returned after calling pth(t, 5). 


                            

# def  pth(t, n): 
#   """
#     pth(t, n) 
#     [7, 3, 6, 5]        # returns list

# pth(t, 10)    # returns None 
# None
#   """


def tree(root, branches=[]): 
  for branch in branches: 
    assert is_tree (branch), 'branches must be trees' 
  return [root] + list(branches) 

def root(tree): 
  return tree[0] 

def branches (tree): 
  return tree[1:] 

def is_tree (tree): 
  if type(tree) != list or len (tree) < 1: 
    return False 
  for branch in branches(tree): 
    if not is_tree (branch): 
      return False 
  return True

def is_leaf (tree): 
  return not branches(tree)

t=tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)]) 
# [1, [3, [4], [5], [6]] , [2] ] 
root(t) 
# 1 
branches(t) 
# [1, [3, [4], [5], [6]] , [2] ] 
root(branches(t)[0]) 
# 3 
is_leaf(t) 
# False 
is_leaf(branches(t)[1]) 
# True

def count_leaves(tree): 
  if is_leaf(tree): 
    return 1 
  else: 
    branch_counts = [count_leaves(b) for b in branches(tree) ] 
    return sum (branch_counts)

print(count_leaves(t)) # 4

def pth(t, n):
    if not(is_tree(t)):
        print("not tree")
        return

    def findPath(t, allPath, n):            
        if is_leaf(t) and t[0] != n:
            allPath.pop()
        
        allPath.append(t[0])
        if len(t) > 2:
            lFound = findPath(t[1], allPath, n)
            rFound = findPath(t[2], allPath, n)
            if len(allPath) == 1 and allPath[0] != n:
                return None
            if not (n in allPath):
                return allPath + [n]
            return allPath
        
        elif len(t) > 1:
            return findPath(t[1], allPath, n)
        
        else:
            if t[0] != n:
                allPath.pop()
            else:
                return allPath

    return findPath(t, [], n)


t2 = tree(7,
        [tree(3, [tree(4, [tree(8)]), tree(6, [tree(5), tree(11)])]),
        tree(15, [tree(13)])]
    )
print(t2)

print(pth(t2, 5)) #[7, 3, 6, 5]
print(pth(t2, 10)) #None
print(pth(t2, 13)) # [7, 15, 13]
print(pth(t2, 8))  # [7, 3, 4, 8]
