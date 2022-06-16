#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter

def pickingNumbers_0(a) -> int:
    """
    We choose the following multiset of integers from the array: . 
    Each pair in the multiset has an absolute difference  (i.e., , , and ), 
    so we print the number of chosen integers, , as our answer.
    return:
    int: the length of the longest subarray that meets the criterion

    >>> a = [4, 6, 5, 3, 3, 1]
    >>> pickingNumbers_0(a)
    3
    >>> a = [1, 2, 2, 3, 1, 2]
    >>> pickingNumbers_0(a)
    5
    """
    a = Counter(a)
    res = 0
    for k in sorted(a):
        m = a[k]+a.get(k+1,0)
        if res<m:
            res=m
    return res

def pickingNumbers_1(a) -> int:
    """
    Uisng list comperhension
    """
    a = Counter(a)
    return max(a[k]+a.get(k+1,0) for k in sorted(a))


def pickingNumbers(a) -> int:
    """
    We choose the following multiset of integers from the array: . 
    Each pair in the multiset has an absolute difference  (i.e., , , and ), 
    so we print the number of chosen integers, , as our answer.
    return:
    int: the length of the longest subarray that meets the criterion

    >>> a = [4, 6, 5, 3, 3, 1]
    >>> pickingNumbers_0(a)
    3
    >>> a = [1, 2, 2, 3, 1, 2]
    >>> pickingNumbers_0(a)
    5
    """
    res = 0
    for i in a:
        t_0 = a.count(i) 
        t_1 = a.count(i+1)
        if res < t_0 + t_1:
            res = t_0 + t_1
    return res

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
