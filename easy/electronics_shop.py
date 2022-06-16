#!/bin/python3

import os
import sys

#
# A person wants to determine the most expensive computer keyboard 
# and USB drive that can be purchased with a given budget. 
# Given price lists for keyboards and USB drives and a budget, 
# find the cost to buy them. 
# If it is not possible to buy both items, return -1.
#

def getMoneySpent(keyboards, drives, b):
    """
    >>> b = 10
    >>> keyboards, drives = [3, 1], [5, 2, 8]
    >>> getMoneySpent(keyboards, drives, b)
    9
    >>> b = 5
    >>> keyboards, drives = [40,50,60], [5,8,12]
    >>> getMoneySpent(keyboards, drives, b)
    58
    >>> b = 60
    >>> keyboards, drives = [4], [5]
    >>> getMoneySpent(keyboards, drives, b)
    -1
    """
    res = -1

    for x in keyboards:
        for y in drives:
            z = x + y
            if z > res and z <= b:
                res = z
    return res


def getMoneySpent_0(keyboards, drives, s):
    """
    >>> b = 10
    >>> keyboards, drives = [3, 1], [5, 2, 8]
    >>> getMoneySpent(keyboards, drives, b)
    9
    >>> b = 5
    >>> keyboards, drives = [40,50,60], [5,8,12]
    >>> getMoneySpent(keyboards, drives, b)
    58
    >>> b = 60
    >>> keyboards, drives = [4], [5]
    >>> getMoneySpent(keyboards, drives, b)
    -1
    """
    return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= s]+[-1])


def getMoneySpent_1(keyboards, drives, s):
    """
    >>> b = 10
    >>> keyboards, drives = [3, 1], [5, 2, 8]
    >>> getMoneySpent(keyboards, drives, b)
    9
    >>> b = 5
    >>> keyboards, drives = [40,50,60], [5,8,12]
    >>> getMoneySpent(keyboards, drives, b)
    58
    >>> b = 60
    >>> keyboards, drives = [4], [5]
    >>> getMoneySpent(keyboards, drives, b)
    -1
    """
    res = [-1]
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                res.append(i+j)
    return max(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
