def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    python -m doctest -v disc04.py
    >>> count_stair_ways(4)
    5
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)     

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        '''the while loops corresponds to count_k(n-1)+count_k(n-2)+count_k(n-3)
        ----count_k(n-k)'''
        while i <= k:
            total += count_k(n - i,k)
            i +=1
    return total        

def even_weighted(s):#even是偶数
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    
    temp = []
    temp1 = []
    if len(s) == 0:
        return 1
    for i in range(2,len(s)):
        temp = s[::i]
        temp2 = 1 
        for j in range(len(temp)):
            if temp2 * temp[j] > temp2:
                temp2 = temp2 * temp[j]
        temp1.append(temp2)    #存储每次的最大值    
    return max(temp1)          
# if __name__ == "__main__":
#     print(max_product([10,3,1,9,2]))

    # temp1 = 0
    # temp2 = 0
    # max = 0
    # for i in range(len(s)-1):
    #     temp1 = s[i]
    #     for j in range(i+1,len(s)):
    #         temp2 = s[j]
    #         if temp1 * temp2 > max:
    #             max = temp1 * temp2
    # return max 