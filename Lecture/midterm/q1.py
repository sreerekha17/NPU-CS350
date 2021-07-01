empty = []
def is_LL(s):
  return s == empty or (len(s) == 2 and is_LL(s[1]))

def LL(first, rest):
  assert is_LL(rest), "rest must be a singly linked list"
  return [first, rest]

ls = LL(1, LL(2, LL(3, empty))) 
# ls
# [1, [2, [3, []]]]

##
# Determine DNA sequence C A T C A T
##

def det(ll):
  if (not ll) or not(len(ll)):
    return False
  dnaSequence = ['C', 'A', 'T', 'C', 'A', 'T']
  
  def isMatch(ll, sequence):
    # print(ll, sequence)
    if(not(len(ll))):
      return False
    elif(not(len(sequence))):
      return True
    elif(ll[0] == sequence[0]):
      return isMatch(ll[1], sequence[1:])
    else:
      return isMatch(ll[1], dnaSequence)
  return isMatch(ll, dnaSequence)
    


dna = LL('C', LL('A', LL('T', empty)))
dna = LL('C', LL('A', LL('T', LL('G', dna))))

print(det(dna)) #False

end = LL('T', LL('C', LL('A', LL('T', LL('G', empty)))))
dna = LL('G', LL('T', LL('A', LL('C', LL('A', end)))))
print(det(dna)) #True
