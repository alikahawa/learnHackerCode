#!/bin/python3

import os
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    """
    The heiest letter times the length of the word, is equal to the highlight
    When we want to highlight a text in a pdf or any other tes, we can add a rectangle 
    that has the area = the height of a letter x the length of the word!
    
    input:
    h = 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    word = abc

    output:
    9

    >>> h= 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
    >>> word = zaba
    >>> designerPdfViewer(h, word)
    28
    
    """
    alphabet_list = list(string.ascii_lowercase)
    max_height = 0
    
    for letter in word:
        letter_index = alphabet_list.index(letter)
        hight_letter = h.__getitem__(letter_index)
        if max_height < hight_letter:
            max_height = hight_letter
    
    res = max_height * len(word)
    print(res)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
