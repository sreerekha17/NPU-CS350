# 1.   Write add_course function to add a course to the program of the curriculum in a tree structure at a university. You should not be able to add a course to a course or to a program that doesn't exist. def tree(root, branches=[]):   for branch in branches:     assert is_tree (branch), 'branches must be trees'   return [root] + list(branches) def root(tree):   return tree[0] def branches (tree):   return tree[1:] def is_tree (tree):   if type(tree) != list or len (tree) < 1:     return False   for branch in branches(tree):     if not is_tree (branch):       return False   return Truedef is_leaf (tree):   return not branches(tree)def add_course (t, course, prog):"""Returns a new tree with course added to prog. Assume the prog already exists.  t = tree('Engineering Sch',                    [tree('BSCS'), [tree('Networking')],                     tree('MSCS', [tree('Machine Learning'), tree('Intro to AI')]),                    tree('MSEE'), [tree('Embedded Sys design')]]           )
#   course = 'Reinforcement Learning'  prog = 'MSCS'  add_course (t, course, prog)  #------- Function return value ------------  ['Engineering Sch',  ['BSCS'],  [['Networking']],  ['MSCS', ['Machine Learning'], ['Intro to AI'], ['Reinforcement Learning']],  ['MSEE'],  [['Embedded Sys design']]]  """


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


"""def add_course (t, course, prog):
  Returns a new tree with course added to prog. Assume the prog already exists.
    i
  t = tree('Engineering Sch', 
                   [tree('BSCS'), [tree('Networking')], 
                    tree('MSCS', [tree('Machine Learning'), tree('Intro to AI')]),
                    tree('MSEE'), [tree('Embedded Sys design')]] 
          )
          
  course = 'Reinforcement Learning'
  prog = 'MSCS'
  add_course (t, course, prog)

  #------- Function return value ------------
  ['Engineering Sch',
  ['BSCS'],
  [['Networking']],
  ['MSCS', ['Machine Learning'], ['Intro to AI'], ['Reinforcement Learning']],
  ['MSEE'],
  [['Embedded Sys design']]]

  """

#Solution

def add_course (t, course, prog):
    if not(is_tree(t)):
        print("Given tree is not a binary tree")
        return

    foundProgram = None
    for branch in branches(t):
        if branch[0] == prog:
            foundProgram = branch
        for b in branch:
            if b[0] == prog:
                foundProgram  = branch

    if foundProgram:
        foundProgram.append(tree(course))
    else:
        print("Could not find program", prog)

t = tree('Engineering Sch', 
            [tree('BSCS'), [tree('Networking')], 
            tree('MSCS', [tree('Machine Learning'), tree('Intro to AI')]),
            tree('MSEE'), [tree('Embedded Sys design')]] 
          )
print("Original Tree", t)

add_course(t, 'Reinforcement Learning', 'MSEE')

print("After adding the course", t)

#non-existent course
add_course(t, 'Reinforcement Learning', 'MSEEE')
