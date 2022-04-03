#!/bin/python3

import math
import os
import random
import re
import sys

"""
Staircase detail

This is a staircase of size n = 4 :

   #
  ##
 ###
####
"""
def staircase(n: int) -> str:
    res = ""
    for i in range(1,n+1):
        if i == n:
            res = res + " " * (n-i) + "#" * i
        else:
            res = res + " " * (n-i) + "#" * i + "\n"
    print(res)

def staircase_v1(n: int) -> str:
    "This solution is shorter"
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*(i))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
