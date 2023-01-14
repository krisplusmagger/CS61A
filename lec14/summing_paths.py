from tree import *

numbers = tree(3, [tree(4), tree(5, [tree(6)])])

haste = tree('h', [tree('a', [tree('s'),
                              tree('t')]),
                   tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
t = tree(3, [tree(-1), tree(2, [tree(1)]), tree(1, [tree(-1)])])

def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])    
        
