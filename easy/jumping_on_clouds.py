#!/bin/python3

import os

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
"""
here is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
"""

def jumpingOnClouds(c):
    """
    >>> c = [0, 0 ,1, 0, 0, 1, 0]
    >>> jumpingOnClouds(c)
    4

    >>> c = [0, 0 , 0, 0, 1, 0]
    >>> jumpingOnClouds(c)
    3
    
    """
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])



def jumpingOnClouds_V1(c):
    """
    >>> c = [0, 0 ,1, 0, 0, 1, 0]
    >>> jumpingOnClouds(c)
    4

    >>> c = [0, 0 , 0, 0, 1, 0]
    >>> jumpingOnClouds(c)
    3
    """
    res, i = 0, 0
    while i < len(c)-2:
        if c[i + 2]:
            i = i + 1
        else:
            i = i + 2
        res += 1
    if i < len(c)-1:
        res+=1
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
