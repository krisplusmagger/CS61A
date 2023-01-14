def palindrome(s):
    """Return whether s is the same backward and forward.
    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seven eves')
    False
    """
    # 替代
    # return all([a == b for a, b in zip(s, reversed(s))])
    return s == list(reversed(s))

def count_partitions(n, m):
    """count partitions
    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return exact_match + with_m + without_m            
