# Write a function path_exist(t, string) that takes in a tree t and a string. 
# It returns True if there is a path in a tree where the path contains "string", otherwise, returns False


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

def  path_exist(t, string):
    """
    Returns True if there is a path in a tree where the path
    contains "string", otherwise, returns False
    e.g. 

    t = tree('p', 
        [tree('i'),
         tree('y', [tree('t', [tree('h', [tree('o'), tree('n')])]),
         tree('m')])]
        )

    path_exist(t, 'p')
    True
    path_exist(t, 'i')
    True
    path_exist(t, 'pi')
    True
    path_exist(t, 'the')
    False
    path_exist(t, 'python')
    True
    path_exist(t, 'hot')
    False

    """

    if not(tree(t)):
      print("Invalid tree provided")
      return


    def findIfExists(t, _str, result):
      # print(t, _str, result)
      if not(len(_str)): #all match found
        return True
      else:
        if t[0] == _str[0]:
          result.append(t[0])
          _str = _str[1:]

          if len(_str):
            if len(t) >= 2:
              exists = False
              for i in range(1, len(t)):
                exists = findIfExists(t[i], _str, result)
                if exists:
                  return True
          else:
            return True
        elif len(t) >= 2:
          exists = False
          for i in range(1, len(t)):
            exists = findIfExists(t[i], _str, result)
            if exists:
                  return True
        else:
          return False

    return ( findIfExists(t, string, []) or False)

t = tree('p', 
        [tree('i'),
         tree('y', [tree('t', [tree('h', [tree('o', [tree('n')])])]),
         tree('m')])]
        )

print('p \t',  path_exist(t, 'p')) #True
print('i \t', path_exist(t, 'i'))  #True
print('pi \t', path_exist(t, 'pi'))
print('the \t', path_exist(t, 'the')) #False
print('python \t', path_exist(t, 'python')) #True
print('hot \t', path_exist(t, 'hot')) #False