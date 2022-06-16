#!/bin/python3
# This problem is too easy, but catching the input is good

import os



def difference(x, y):
    if x-y < 0:
        return y-x
    else:
        return x-y

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if difference(x, z) < difference(y,z):
        return "Cat A" 
    if difference(y, z) < difference(x,z):
        return "Cat B" 
    else:
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()


# it can also be approached as seperate script:
# q = int(input().strip())
# for a0 in range(q):
#     x,y,z = input().strip().split(' ')
#     x,y,z = [int(x),int(y),int(z)]
#     if abs(x-z)>abs(y-z):
#         print('Cat B')
#     elif abs(x-z)<abs(y-z):
#         print('Cat A')
#     else:
#         print('Mouse C')