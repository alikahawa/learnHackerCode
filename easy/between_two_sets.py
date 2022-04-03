#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    """
    The elements of the first array are all factors of the integer being considered
    The integer being considered is a factor of all elements of the second array
    
    >>> a = [3, 4]
    >>> b = [24, 48]
    >>> getTotalX_v1(a, b)
    2
    """
    res=0
    for i in range(1, 101):
        if all(i%x==0 for x in a) and all(x%i==0 for x in b):
            res+=1
    print(res)
    return res

def is_after(x, arr):
    """
    The elements of the array are all factors of the integer being considered (x)
    """
    for i in arr:
        if x % i != 0:
            return False
    return True

def is_before(x, arr):
    """
    The integer being considered (x) is a factor of all elements of the array
    """
    for i in arr:
        if i % x != 0:
            return False
    return True

def getTotalX_v1(a, b):
    """
    The elements of the first array are all factors of the integer being considered
    The integer being considered is a factor of all elements of the second array

    >>> a = [3, 4]
    >>> b = [24, 48]
    >>> getTotalX_v1(a, b)
    2
    """
    res_arr = [x for x in range(1, 101) if is_after(x, a) and is_before(x, b)]
    return len(res_arr)

if __name__ == '__main__':
    """
    input example:
    2 3
    2 4
    16 32 96

    output:
    3
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
