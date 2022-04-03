#!/bin/python3

import math
import os
from collections import Counter


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    """
    This solution is applicable to all languages!
    """
    arr_res = [0] * 6 # an array with 0 values
    for i in arr:
        arr_res[i] += 1
    print(arr_res)
    res, max_value = 0, 0
    for i in arr_res:
        if i > max_value:
            max_value = i
            res = arr_res.index(i)
    return max(arr_res)

def migratoryBirds(arr):
    """
    Only python solution!
    """
    mydict = dict(Counter(arr))
    res = max(mydict, key=mydict.get)  
    print(res)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
