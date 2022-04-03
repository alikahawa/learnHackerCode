

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    """
    >>> s = [1,2,1,3,2]
    >>> d = 3
    >>> m = 2
    >>> birthday(s,d,m)
    2
    >>> s = [1,1,1,1,1,1]
    >>> d = 3
    >>> m = 2
    >>> birthday(s,d,m)
    0
    >>> s = [4]
    >>> d = 4
    >>> m = 1
    >>> birthday(s,d,m)
    1

    """
    res = 0
    for i in range(m, n+1):
        # take the sum of the subarray from i-m to i 
        if sum(s[i-m:i]) == d:
            res += 1
    print(res)
    return res

def birthday_v1(s, d, m):
    """
    >>> s = [1,2,1,3,2]
    >>> d = 3
    >>> m = 2
    >>> birthday_v1(s,d,m)
    2
    >>> s = [1,1,1,1,1,1]
    >>> d = 3
    >>> m = 2
    >>> birthday_v1(s,d,m)
    0
    >>> s = [4]
    >>> d = 4
    >>> m = 1
    >>> birthday_v1(s,d,m)
    1
    """
    res = 0
    squares = 0
    for i in range(0,m):
        squares += s[i]
    if squares == d:
        res += 1

    for i in range(1, n-m+1):
        squares += s[i+m-1] - s[i-1]
        if squares == d:
            res += 1
    print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
