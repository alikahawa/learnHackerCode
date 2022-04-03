#!/bin/python3


import os

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    max_count = 0
    for i in arr:
        curr = arr.count(i)
        if curr > max_count:
            max_count = curr
            
    return len(arr) - max_count

def equalizeArray_v1(arr):
    return (len(arr) - arr.count(max(set(arr), key = arr.count)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
