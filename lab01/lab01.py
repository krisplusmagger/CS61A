def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    # num = 1
    # for i in range(k+1,n+1):
    #     num *= i
    # return num
    """递归实现"""
    if(n == k + 1):
        return n 
    else:
     
        return n * falling(n-1,k)
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    if(y == 0):
        return y
    else:

        return y % 10 + sum_digits(y//10)     #y % 10 是最后一位数，y//10是原数去掉最后一位数


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n != 0:
        last_num = n % 10
        n = n // 10
        last_num2 = n % 10
        if(last_num == 8 and last_num2 == 8):
            return True
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while(n != 0):
        last_num = n % 10
        if(has_digit(n//10, last_num) != True):
            i = i + 1
        n = n // 10    
    return i        


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while(n!=0):
        last = n % 10 
        if k == last:
            return True
        n = n // 10    
    return False    


