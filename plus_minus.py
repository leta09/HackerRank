#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    plus = [i for i in arr if i>0]
    minus = [i for i in arr if i < 0]
    zero = [i for i in arr if i ==0]
    
    
    print("%.6f" % (len(plus)/len_arr))
    print("%.6f" % (len(minus)/len_arr))
    print("%.6f" % (len(zero)/len_arr))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))