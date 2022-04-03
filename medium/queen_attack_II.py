#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Complete the queensAttack function in the editor below.

    queensAttack has the following parameters:
    - int n: the number of rows and columns in the board
    - nt k: the number of obstacles on the board
    - int r_q: the row number of the queen's position
    - int c_q: the column number of the queen's position
    - int obstacles[k][2]: each element is an array of 2 integers, the row and column of an obstacle

    >>>
    >>>
    """



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()



"""

n, k = map(int, input().split())
rq, cq = map(int, input().split())

moves = {'n': n - rq, 'nw': min(n - rq, cq-1), 'ne': min(n - rq, n - cq),
         's': rq-1, 'sw': min(rq-1, cq-1), 'se': min(rq-1, n - cq), 'w': cq-1, 'e': n - cq}
for _ in range(k):
    r, c = map(int, input().split())
    if c == cq:
        if r > rq:
            moves['n'] = min(r-rq-1, moves['n'])
        else:
            moves['s'] = min(rq-r-1, moves['s'])
    elif r == rq:
        if c > cq:
            moves['e'] = min(c-cq-1, moves['e'])
        else:
            moves['w'] = min(cq-c-1, moves['w'])
    elif c - r == cq - rq:
        if c < cq and r < rq:
            moves['sw'] = min(min(cq-c-1, rq-r-1), moves['sw'])
        elif c > cq and r > rq:
            moves['ne'] = min(min(c-cq-1, r-rq-1), moves['ne'])
    elif c + r == cq + rq:
        if c < cq and r > rq:
            moves['nw'] = min(min(r-rq-1, cq-c-1), moves['nw'])
        elif c > cq and r < rq:
            moves['se'] = min(min(rq-r-1, c-cq-1), moves['se'])
            
print(sum(moves.values()))


"""