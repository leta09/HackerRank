#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_score = scores[0]
    lowest_score= scores[0]
    high = 0
    low = 0
    for i in scores[1:]:
        if i > highest_score:
            high += 1
            highest_score = i
        if i < lowest_score:
            low +=1
            lowest_score = i
    return [high, low]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
   
