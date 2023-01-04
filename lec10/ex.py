def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)    
''''shorter a version'''        
def cascade_shorter(n):
    print(n)
    if n > 10:
        cascade_shorter(n // 10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)  

from ucb import trace

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1     
    else:
      
        return fib(n-1) + fib(n-2)        

def count_partitions(n, m):

    if n == 0:
        return 1
    elif n < 0:
        return 0 
    elif m == 0:
        return 0

    else:
        return count_partitions(n-m, m)+ count_partitions(n, m-1)

