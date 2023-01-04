def count(s, value):
    '''count the number of times that valued the 
    same in sequence
    >>> count([1,2,1,2,1],1)
    3
    '''
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total        

def unpack(pairs):
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count      
def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total
def cheer():
    for _ in range(3):
        print("Go bears!") 

def divisors(n):
    '''计算除数'''
    return [x for x in range(1,n+1) if n%x == 0]
