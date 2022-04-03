#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    """
    
    >>> arr = 5 4 4 2 2 8
    >>> cutTheSticks(arr)
    6
    4
    2
    1

    >>> arr = 1 2 3 4 3 3 2 1
    >>> cutTheSticks(arr)
    8
    6
    4
    1
    """
    arr.sort(reverse=True)
    res = []
    while arr:
        print(len(arr))
        res.append(len(arr))
        min_element = arr.pop()
        while arr and min_element == arr[-1]:
            arr.pop()
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
