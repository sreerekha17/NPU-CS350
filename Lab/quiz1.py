empty = []

def is_LL(s):
  return s == empty or (len(s) == 2 and is_LL(s[1]))

def LL(first, rest):
  assert is_LL(rest), "rest must be a singly linked list"
  return [first, rest]

def chk_elm(ls, elem):
  if (not(len(ls)) or not(is_LL(ls)) or not elem):
    print("Error: needs a valid linked list to proceed")
    exit()
  
  current = ls
  while current:
    if(current[0] == elem):
      return True
    else:
      current = current[1]

  return False

"""Return whether ELEM is in the sequence ls 
chk_elm(LL(1, LL(2, LL(3, empty))), 1) 
True 
chk_elm(LL(1, LL(2, LL(3, empty))), 4) 
False 
"""
print(chk_elm(LL(1, LL(2, LL(3, empty))), 1) )
print(chk_elm(LL(1, LL(2, LL(3, empty))), 2) )
print(chk_elm(LL(1, LL(2, LL(3, empty))), 4) )
print(chk_elm(LL(1, LL(2, LL(3, empty))), 14) )
print(chk_elm([], 1))