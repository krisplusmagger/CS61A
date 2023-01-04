def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15 :5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).
    """
    if n == 1:
        return m 
    else:
        return m + multiply(m,n-1)

def rec(x, y):
    '''rec(3,2)'''
    if y > 0:
        return x * rec(x, y - 1)
    return 1

def is_prime(n, i = 2):
    """Returns True if n is a prime number and False otherwise.
    只能被1和本身整除
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if i == n:
        return True 
        
    else:
        if n % i == 0:
            return False
        else:
            i += 1 
            return is_prime(n, i)    

def hailstone(n, i = 1):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    return the number of steps and print each value
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    if n == 1:
        print(n)
        return i 

    elif n % 2 == 0:
        i += 1
        print(n)
        n = n // 2
        return hailstone(n, i)

    elif n % 2 != 0 and n != 1:
        i += 1
        print(n)
        n = n * 3 + 1
        return hailstone(n, i)    

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    输入的是内部递减的数
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    >>> merge(13,0)
    13
    """

    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

         




