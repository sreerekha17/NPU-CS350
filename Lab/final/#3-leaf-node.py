# Define a function add_leaves(t, lst) that takes a tree t, and one dimensional list lst, and produces a new tree by adding all elements in lst to every leaf in t. Do not add them to non-leaf nodes.

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

# def add_leaves(t, lst):

#     """
#     Add new leaves in lst to each leaf in the original tree t and return the new tree.

#     t1 = tree(11, [tree(12), tree(13)])
#     t1: 
#               11
#             /   \
#            12   13    
#     new1 = add_leaves(t1, [4, 5])
#     new1:  
#               11
#             /    \
#            12    13
#           / \    / \
#          4   5  4   5 
#     t2 = tree(11, [tree(12, [tree(13)])])
#     t2: 
#               11
#             /    
#            12    
#           /     
#          13    
#     new2 = add_leaves(t2, [6, 7, 8])
#     new2: 
#               11
#              /    
#             12    
#            /     
#           13 
#         / | \
#        6  7  8
#     """


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

def add_leaves(t, lst):
    if not(is_tree(t)) or lst is None or not(len(lst)):
        print("Please provide valid tree and array to proceed")
        return
    if not(branches(t)):
        for i in lst:
            t.append(tree(i))
        return t
    
    for branch in branches(t):
        if is_leaf(branch):
            for i in lst:
                branch.append(tree(i))
        elif (is_tree(branch)):
            for b in branches(branch):
                if is_leaf(b):
                     for i in lst:
                        b.append(tree(i))

    return t


t1 = tree(11, [tree(12), tree(13)])
print(t1)

new1 = add_leaves(t1, [4, 5])
print(new1)

t2 = tree(11, [tree(12, [tree(13)])])
new2 = add_leaves(t2, [6, 7, 8])
print(new2)

