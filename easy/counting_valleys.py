#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# An avid hiker keeps meticulos records of their hikes
# During the last hike that took exactly `steps` steps, 
# for every step it was noted if it was an uphill, U, 
# or a downhill, D step. Hikes always start and end at sea level, 
# and each step up or down represents a 1 unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, 
# starting with a step up from sea level and ending with a step down to sea level.

# A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.

# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

def countingValleys(steps, path):
    """
    
    >>> steps, path = 8, "UDDDUDUU"
    >>> countingValleys(steps, path)
    1
    >>> steps, path = 10, "DUDUUDDU"
    >>> countingValleys(steps, path)
    3
    >>> steps, path = 12, "DDUUDDUDUUUD"
    >>> countingValleys(steps, path)
    2
    """
    counter, result = 0, 0
    for c in path:
        if c == 'U':
            counter += 1
            if counter == 0:
                result += 1
        if c == 'D':
            counter -= 1
        
    print(result)
    return result   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
