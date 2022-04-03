#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

"""
In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

Divisible by 400.
Divisible by 4 and not divisible by 100.
"""
def dayOfProgrammer(year):
    # Write your code here
    leap_year = 244
    normal_year = 243
    res = 256
    if year == 1918:
        res = str(res - normal_year + 13) + ".09." + str(year)
        return res
    if year > 1919:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            "Leap year"
            res = str(res - leap_year) + ".09." + str(year)
        else:
            res = str(res - normal_year) + ".09." + str(year)
    else:
        if year % 4 == 0:
            res = str(res - leap_year) + ".09." + str(year)
        else:
            res = str(res - normal_year) + ".09." + str(year)             
    return res 
        

def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year

def day_of_programmer(y):
    count=0
    if(y>1918 and y<=2700):
        if(y%400==0 or (y%4==0 and y%100!=0)):
            count=1
        if(count==1):
            print('12.09.'+str(y))
        else:
            print('13.09.'+str(y))
    if(y<1918 and y>=1700):
        if(y%4==0):
            count=1
        if(count==1):
            print('12.09.'+str(y))
        else:
            print('13.09.'+str(y))
    if(y==1918):
        print('26.09.1918')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
