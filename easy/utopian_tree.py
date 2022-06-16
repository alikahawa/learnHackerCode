#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def odd(a):
    return a % 2 == 1

def even(a):
    return a % 2 == 0
    
def utopianTree(n):
    if n == 0:
        return 1
    elif odd(n):
        return 2 * utopianTree(n-1)
    elif even(n):
        return 1 + utopianTree(n-1)


def utopianTree_0(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        if odd(i) and i > 2:
            res = res * 2
        else:
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
