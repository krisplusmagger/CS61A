# Setup: First download the corpus from here, unzip it, and put
#        this source file in the same directory as suppes.parsed
#
# https://www.socsci.uci.edu/~lpearl/CoLaLab/CHILDESTreebank/CHILDESTreebank-curr.zip
#
# For more info, see:
#
# https://www.socsci.uci.edu/~lpearl/CoLaLab/CHILDESTreebank/childestreebank.html


# Trees

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_t(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_t(branch):
            return False
    return True

def is_leaf(t):
    return not branches(t)

def leaves(t):
    """Return a list of the leaf labels of a tree."""
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])

# Syntax

example = tree('FRAG', 
               [tree('NP',
                     [tree('DT', [tree('a')]),
                      tree('JJ', [tree('little')]),
                      tree('NN', [tree('bug')])]),
                tree('.', [tree('.')])])

from string import punctuation
contractions = ["n't", "'s", "'re", "'ve"]

def words(t):
    """Return the words of a tree as a string.

    >>> words(example)
    'a little bug.'
    """
    s = ''
    for w in leaves(t):
        no_space = (w in punctuation and w != '$') or w in contractions
        if not s or no_space:
            s = s + w
        else:
            s = s + ' ' + w
    return s

def replace(t, s, w):
    """Return a tree like T with all nodes labeled S replaced by word W.

    >>> words(replace(example, 'JJ', 'huge'))
    'a huge bug.'
    'JJ' label是形容词
    """
    if label(t) == s:
        return tree(s, [tree(w)])
    else:
        return tree(label(t), [replace(b, s, w) for b in branches(t)])    

# Reading trees

examples = """
(ROOT (SQ (VP (COP is)
     (NP (NN that))
     (NP (NP (DT a) (JJ big) (NN bug))
      (CC or)
      (NP (DT a) (JJ little) (NN bug))))
     (. ?)))

(ROOT (FRAG (NP (DT a) (JJ little) (NN bug)) (. .)))

""".split('\n')

def read_trees(lines):
    """Return trees as lists of tokens from a list of lines.

    >>> for s in read_trees(examples):
    ...     print(s[:10])
    ['(', 'ROOT', '(', 'SQ', '(', 'VP', '(', 'COP', 'is', ')']
    ['(', 'ROOT', '(', 'FRAG', '(', 'NP', '(', 'DT', 'a', ')']
    """
    trees = []
    tokens = [] # toekns可以是单词，标签或者括号
    for line in lines:
        if line.strip():
            tokens.extend(line.replace('(',' ( ').replace(')', ' ) ').spilt())
            


def all_trees(path='CHILDESTreebank-curr/suppes.parsed'):
    return read_trees(open(path).readlines())

# Representing trees

def tree(label, branches=[]):
    if not branches:
        return [label]
    else:
        return ['(', label] + sum(branches, start=[]) + [')']

def label(t):
    if len(t) == 1:
        return t[0]
    else:
        assert t[0] == '(', t
        return t[1]

def branches(t):
    if t[0] != '(':
        return []
    current_branch = []
    all_branches = []
    opened = 1
    for token in t[2:]:
        current_branch.append(token)
        if token == '(':
            opened += 1
        elif token == ')':
            opened -= 1
        if opened == 1:
            all_branches.append(current_branch)
            current_branch = []
    assert opened == 0 and current_branch == [')'], t
    return all_branches

example = tree('ROOT', 
               [tree('FRAG', 
                     [tree('NP',
                           [tree('DT', [tree('a')]),
                            tree('JJ', [tree('little')]),
                            tree('NN', [tree('bug')])]),
                      tree('.', [tree('.')])])])

def replace_all(s, w):
    """Print the result of replace(t, s, w) for all syntax trees t."""
    for t in all_trees():
        r = replace(t, s, w)
        if t != r:
            print('Original: ', words(t).lower())
            print('Replaced: ', words(r).lower()) 
            input() # Wait for the user to press enter/return
        

# replace_all('NNS', 'bears')
# replace_all('NP', 'Oski')
