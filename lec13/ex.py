def rational(n, d):
    '''construct a rational number that represents N/D'''
    from fractions import gcd
    g = gcd(n,d)

    return [n//g, d//g] 

def numer(x):
    '''return the numertator of rational number X
    返回分子'''
    return x[0]

def denom(x):
    '''return the denominator of rational number X
    返回分母'''
    return x[1]

def divide_rational(x, y):
    return [ x[0] * y[1], x[1] * y[0] ]