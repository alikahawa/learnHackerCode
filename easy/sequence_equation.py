#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    """
    p=[5,2,1,3,4]
    Each value of x between 1 and 5, the length of the sequence, is analyzed as follows:
    1. x=1 congruent tp p[3], p[4] = 3, so p[p[4]]=1
    2. x=2 congruent tp p[2], p[2] = 2, so p[p[2]]=2
    3. x=3 congruent tp p[4], p[5] = 4, so p[p[5]]=3
    4. x=4 congruent tp p[5], p[1] = 5, so p[p[1]]=4
    5. x=5 congruent tp p[1], p[3] = 1, so p[p[3]]=5
    """
    f_inverse = dict()
    function = dict()
    res = list()
    for i in range(len(p)):
        function[i+1] = p[i]
        f_inverse[p[i]] = i + 1
    for i in range(1, n+1):
        res.append(f_inverse[f_inverse[i]])
        print(f_inverse[f_inverse[i]])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
