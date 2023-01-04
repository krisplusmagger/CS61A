def search(f):
    x = 0
    while not f(x):
        
        x += 1
    return x
def is_three(x):
    return x == 3
def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    #f是square,y是256,x是从0开始的
    return lambda y: search(lambda a: f(a) == y)        

def if_(c, t, f):
    if c:
        return t
    else:
        return f    

from math import sqrt 

def real_sqrt(x):
    '''Return the real part of the square root of x'''
    return if_(x >=0, sqrt(x),0)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10       

def reasonable(n):
    return n ==0 or 1/n !=0    
from operator import add, mul 
def square(x):
    return mul(x,x)
def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder    