#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# Given a set of distinct integers, print the size of 
# a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.
# 
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
# This will be much more diffecult if we need to return the best set, 
# it can be solved using dynamic programming algorithm which will have 
# a high run time complexity at least O(nm)

def nonDivisibleSubset(k, s):
    """
    >>> k = 3
    >>> s = [1 7 2 4]
    >>> nonDivisibleSubset(k, s)
    3

    >>> k = 7
    >>> s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 
    702, 282, 718, 771, 575, 436]
    >>> nonDivisibleSubset(k, s)
    11
    
    """
    # The steps taken are simple: first we create a 2d array
    d = {x:[] for x in range(k)}

    # We fill the arrays in the 2d array, i.e. d 
    # with the values depending on its reainders
    for i in range(n): 
        d[s[i]%k].append(s[i])

    count = 0
    # The first check, if there are one or more values which are divisble by
    # k then we add one to our result.
    # We are allowed to use only one element from this array
    if len(d[0]) > 0:
        count = 1
    
    # We create a set that contains pairs which take values from
    # 1 until (k//2) + 1 which represent the middle remainder
    # For example: k = 11 ==> k//2 = 5 + 1 = 6 
    arr_set = set([(x,k-x) for x in range(1,k//2+1)])

    for i,j in arr_set:
        if i != j:
            # We take the highest numeber of elements which will never
            # sum to a multiple of k
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:

                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
