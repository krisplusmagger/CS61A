def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x * x

def make_adder(n):
    def adder(K):
        return K + n
    return adder    
def f(x,y):
    def g(x):
        return x + y     
    return g       
def square(x):
    return x * x
def triple(x):
    return 3 * x

def composel(f,g):
    def h(x):
        return f(g(x)) 
    return h              
"""Lambda expression""" 
square = lambda x : x * x

def composel2(n):
    return lambda k: n+ k
def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h 
    return g         