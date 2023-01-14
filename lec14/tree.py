def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]       

def is_tree(tree):
    """a tree must be a list and it has branches, so  its length >= 1
    otherwise, it is a leaf"""
    if type(tree) != list or len(tree) < 1: 
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True            
   
def is_leaf(tree):
    return not branches(tree) #如果branches返回空列表就是叶子

def fib_tree(n):
    if n <= 1:
        return tree(n)#若果长度小于一的话就是叶子
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(i) for i in branches(tree)], [])    
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]# increment leaves for all branches of that tree
        return tree(label(t), bs) #return a new tree with more leaves
def increment(t):
    """Return a tree like t but with all labels incremented"""  
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print('   ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)    
def fact(n):
    fact_times(n, 1)

def fact_times(n, k):
    "Return k * n * (n-1)* .... * 1"
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)                        