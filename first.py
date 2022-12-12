
from operator import floordiv, mod



def divide_exact(n,d=10):
       """Return the quotient and reminder of dividing N by D
       
       >>> q, r = divide_exact(2013, 10)
       >>> q
       201
       >>> r
       3
       """
       return floordiv(n,d), mod(n,d)


def absolute_value(x):
	"""Return the absolute value of x."""
	if x < 0:
		return -x
	elif x==0:
		return 0
	else:
		return x
def prime_factors(n):
	"""Print the prime factors of n in none decreasing order
        >>> prime_factors(8)
        2
	2
	2
	>>> prime_factors(9)
	3
	3
	>>> prime_factors(16)
	2
	5
        >>> prime_factors(11)
	11
	>>> prime_factors(12)
	2
	2
	3
	>>> prime_factors(858)
	2
	3
	11
	13
	"""
	while n > 1:
		k = smallest_prime_factor(n)
		n = n // k
		print(k)
def smallest_prime_factor(n):
	"""Return the smallest k > i that evenly divides n."""
	k = 2
	while n % k != 0:
		k = k + 1
	return k
