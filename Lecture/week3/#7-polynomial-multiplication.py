## Problem 7:
# Implement two-polynomial multiplication operation (convolution) by a program conv_LL(l, m)
	# 	e.g.	 
	# Hint: take Polynomial-1.py & Polynomial-2.py as reference in file 
	# 	   Linked List Example-2.zip
##


##
# Referenced from Example polynomial Linked List Example 2
##
class PolynomialNode():
  def __init__(self, degree = None, coefficient = None):
    self.degree = degree
    self.coefficient = coefficient
    self.next = None

class Polynomial():
  def __init__(self, degree=None, coefficient=None):
    if degree is None:
      self.polyHead = None
    else:
      self.polyHead = PolynomialNode(degree, coefficient)
    self.polyTail = self.polyHead
  
  def __add__(self, polyToAdd):
    if (not(self.polyHead.degree >= 0) or not(polyToAdd.polyHead.degree >= 0)):
      raise Exception("Cannot add empty polynomials")

    selfHead = self.polyHead
    otherHead = polyToAdd.polyHead

    newPolynomial = Polynomial()
    
    while selfHead is not None and otherHead is not None:
      if (selfHead.degree > otherHead.degree):
        degree = selfHead.degree
        coefficient = selfHead.coefficient
        selfHead = selfHead.next
      elif (selfHead.degree < otherHead.degree):
        degree = otherHead.degree
        coefficient = otherHead.coefficient
        otherHead = otherHead.next
      else:
        degree = selfHead.degree
        coefficient = selfHead.coefficient + otherHead.coefficient
        selfHead = selfHead.next
        otherHead = otherHead.next
      newPolynomial.appendTerm(degree, coefficient)

    while selfHead is not None:
      newPolynomial.appendTerm(selfHead.degree, selfHead.coefficient)
      selfHead = selfHead.next
    
    while otherHead is not None:
      newPolynomial.appendTerm(otherHead.degree, otherHead.coefficient)
      otherHead = otherHead.next
    
    return newPolynomial
  
  def appendTerm(self, degree, coefficient):
    newTerm = PolynomialNode(degree, coefficient)
    if(not(self.polyHead)):
      self.polyHead = newTerm
    else:
      self.polyTail.next = newTerm
    self.polyTail = newTerm

  def multiplyRootByNode(self, node):
    finalPolynomial = Polynomial()

    currentTerm = self.polyHead
    while currentTerm is not None:
      newDegree = currentTerm.degree + node.degree
      newCoefficient = currentTerm.coefficient * node.coefficient

      finalPolynomial.appendTerm(newDegree, newCoefficient)

      currentTerm = currentTerm.next

    return finalPolynomial

  def __mul__(self, polynomialToMultiply):
    if(not (self.polyHead) or not(polynomialToMultiply.polyHead)):
      raise Exception("Cannot multiply empty polynomial")
    node = self.polyHead
    productPolynomial = polynomialToMultiply.multiplyRootByNode(node)
    node = node.next
    
    while node:
      polyAfterMultiplyByNode = polynomialToMultiply.multiplyRootByNode(node)
      productPolynomial += polyAfterMultiplyByNode
      node = node.next

    return productPolynomial
  
  def printPolynomial(self):
    current = self.polyHead
    content = ''
    while current:
      if (content != ''):
        content += f'+{current.coefficient}x^{current.degree}'
      else:
        content += f'{current.coefficient}x^{current.degree}'
      current = current.next
    print(content)

polynomial1 = Polynomial(5, 4)
polynomial1 += Polynomial(3, 3)
polynomial1 += Polynomial(2, 2)
polynomial1 += Polynomial(0, 1)

polynomial2 = Polynomial(4, 8)
polynomial2 += Polynomial(3, 7)
polynomial2 += Polynomial(1, 6)
polynomial2 += Polynomial(0, 5)

multiple = polynomial1 * polynomial2

multiple.printPolynomial()