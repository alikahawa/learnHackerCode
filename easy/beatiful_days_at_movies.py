#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

"""
We can reverse a number in python using two ways:
"""
def reverse_0(num: int) -> int:
    res = 0
    while num != 0:
        digit = num % 10
        res = res * 10 + digit
        num // 10
    return res

def reverse(num: int) -> int:
    return int(str(num)[::-1])

def beautifulDays(i, j, k):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
