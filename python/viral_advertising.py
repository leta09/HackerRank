#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    liked = 0
    shared = 5
    total = 0
    for i in range(n):
            liked = math.floor(shared/2)
            shared = liked*3
            total +=liked
    return total
        
if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)
    