# Tree structure can be represented by a list of list structure in Python as follows
	
# The following example tree functions can be taken as references for a tree built-up and some operations      
 
# def tree(root, branches=[]): 
#   for branch in branches: 
#     assert is_tree (branch), 'branches must be trees' 
#   return [root] + list(branches) 

# def root(tree): 
#   return tree[0] 

# def branches (tree): 
#   return tree[1:] 

# def is_tree (tree): 
#   if type(tree) != list or len (tree) < 1: 
#     return False 
#   for branch in branches(tree): 
#     if not is_tree (branch): 
#       return False 
#   return True

# def is_leaf (tree): 
#   return not branches(tree)

# t=tree(1, [tree(3, [tree(4), tree(5), tree(6)]), tree(2)]) 
# # [1, [3, [4], [5], [6]] , [2] ] 
# root(t) 
# # 1 
# branches(t) 
# # [ [3, [4], [5], [6]] , [2] ] 
# root(branches(t)[0]) 
# # 3 
# is_leaf(t) 
# # False 
# is_leaf(branches(t)[1]) 
# # True

# def count_leaves(tree): 
#   if is_leaf(tree): 
#     return 1 
#   else: 
#     branch_counts = [count_leaves(b) for b in branches(tree) ] 
#     return sum (branch_counts)

# count_leaves(t)
# # 4

# Write a function hght(t) that returns the height of a tree.

# def hght(t): 
#   """Return the height of a tree
#      t – a list of list structure tree 
#   """
	


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
# [ [3, [4], [5], [6]] , [2] ] 
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

print(count_leaves(t))# 4

# Write a function hght(t) that returns the height of a tree.

def hght(t):    
    if t is None:
        return 0
    else:
      h = 1
      for b in branches(t):
        if is_tree(b):
          for _b in branches(b):
            if branches(_b):
              h += 1
          h +=1
      return h

    

print("height of tree", hght(t))


t2 = tree(1, 
  [tree(3, 
    [tree(4), tree(5), tree(6, [tree(7)])]), 
  tree(2, [tree(100)])]) 

print("height of t2", hght(t2))
