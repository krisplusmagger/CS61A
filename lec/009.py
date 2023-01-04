def trace1(fn):
    '''returns a version of the first function
    it is called'''
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced
@trace1        
def square1(x):
    return x * x

#trace function is called decorator
@trace1
def triple(x):
    return 3 * x  
'''it is identical to''' 
def triple2(x):
    return 3 * x 
triple2 = trace1(triple2)       