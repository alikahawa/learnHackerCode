#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p

# When they flip page 1, they see pages 2 and 3. 
# Each page except the last page will always be printed on both sides. 
# The last page may only be printed on the front, given the length of the book. 
# If the book is n pages long, and a student wants to turn to page p, 
# what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

# Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page .


def pageCount_v0(n, p):
    """
    >>> n, p = 5, 3
    >>> pageCount(5,3)
    1
    >>> n, p = 6, 2
    >>> pageCount(6, 2)
    1
    >>> n, p = 5, 4
    >>> pageCount(5, 4)
    0
    """
    page_in_book = p//2
    total_pages = n//2

    from_front = page_in_book
    from_back = total_pages - page_in_book
    res = min(from_front,from_back)
    print(res)
    return res

def pageCount(n, p):
    """
    >>> n, p = 5, 3
    >>> pageCount(5,3)
    1
    >>> n, p = 6, 2
    >>> pageCount(6, 2)
    1
    >>> n, p = 5, 4
    >>> pageCount(5, 4)
    0
    """
    res = min(p//2,n//2-p//2)
    print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
