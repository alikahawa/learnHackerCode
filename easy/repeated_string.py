#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    if len(s) < 2 and s == "a":
        return n
    
    # s[:y] = only last y elements
    # s[y:] = only first y elements
    y = n % len(s) # = remainder
    x = n // len(s) # = divisor 
    
    # x, y = divmod(n, len(s)) 
    # This will return the result of the division and the remainder
    # this can also be achieved using x,y = divmod(n, len(s))

    return s[:y].count("a")*(x+1) + s[y:].count("a")*x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
