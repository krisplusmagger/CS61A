""" Generalization"""

from math import pi, sqrt



def area(r, shape_constant):
	assert r > 0, 'A length must be positive'
	return r * r  * shape_constant

def area_square(r):
	assert r > 0, 'A length must be positive'
	return area(r, 1)

def area_circle(r):
	return area(r, pi)

def area_hexagon(r):
	return area(r, 3 * sqrt(3) / 2)

def identity(k):
	return k

def cube(k):
	return pow(k,3)
def summation(n, term):
	"""sum the first N terms of a sequence
	
	>>> summation(5,cube)
	225	
	"""
	total, k = 0 , 1
	while k <= n:
		total, k = total + term(k), k + 1
	
	return total 

def make_adder(n):
	"""Return a function that takes one argumentK
	and return K + n
	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(K):
		return K + n
	return adder 	
