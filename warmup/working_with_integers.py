#!/bin/python3

"""
This file contains basic algorithms that mainely works on integers.
"""

import math
import os
import random
import re
import sys

from numpy import min_scalar_type


def miniMaxSum(arr):
   """
   Given five positive integers, 
   find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
   Then print the respective minimum and maximum values as a single line of two space-separated long integers.

   This solution is fast, one iteration ==> O(n)
   """ 
   min_num = sys.maxsize
   max_num = all_sum =0
   for i in arr:
       all_sum = all_sum + i
       if max_num < i:
           max_num = i
           
       if min_num > i:
           min_num = i
   print(all_sum - max_num, " ", all_sum - min_num)

def miniMaxSum_v0(arr):
   """
   Given five positive integers, 
   find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
   Then print the respective minimum and maximum values as a single line of two space-separated long integers.

   This solution is a bit slower, 3 iterations (sum, min, max)
   """ 
   x = sum(arr)
   print (x-(max(arr))), (x-(min(arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
