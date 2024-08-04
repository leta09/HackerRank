#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    res = []
    dif = []
    mi = 0
    temp = list(zip(sorted(arr), sorted(arr)[1:]))
    for i, j in temp:
        dif.append(abs(i-j))
    mi = min(dif)
    for i,j in temp:
        if abs(i-j) == mi:
            res.append(i)
            res.append(j)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()