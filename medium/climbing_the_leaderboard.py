#!/bin/python3

from bisect import bisect_left
from collections import Counter
import os
import copy

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
# Check this https://www.youtube.com/watch?v=CAyXHTqBIBU&list=PLSIpQf0NbcCltzNFrOJkQ4J4AAjW3TSmA 
# Using binary search (working with java, no libraries are used)

def climbingLeaderboard_(ranked, player):
    # Write your code here
    res = []
    counts = Counter(ranked)
    counts = sorted(counts)
    n = len(counts)
    for a in player:
        i = bisect_left(counts, a)
        if i < n and counts[i]==a:
            # print(n - i)
            res.append(n-i)
        else:
            # print(n+1-i)
            res.append(n+1-i)
    return res

        
def climbingLeaderboard_0(ranked, player):
    # didn't pass all, work on time complexity
    res = []
    ranking = []
    for i in player:
        temp = copy.deepcopy(ranked)
        temp.append(i)
        temp = sorted(list(set(temp)))
        ranke = len(temp)
        for j in temp:
            ranking.append((j, ranke))
            if j == i:
                res.append(ranke)
            ranke = ranke - 1
        # print(ranking)
        # for(value, key) in ranking:
        #     if value == i:
        #         res.append(key)
        ranking = []

    # print(res)
    return res
            
def climbingLeaderboard_1(scores,alice):
    """
    
    """
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores)-1
    while score_index!=len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index>-1:
            highscore_index-=1
            if scores[highscore_index]!=scores[highscore_index+1]:
                currentrank-=1
        if alice[score_index] == scores[highscore_index]:
            yield currentrank 
        else:
            yield currentrank+1
        score_index+=1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
