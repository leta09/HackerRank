#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    
    # for i in range(n+1):
    #     print((" "*(n-i))  + i*"#")
    n= n+1
    for i in range(n):
        print(n*" " + "#"*i)
        n-=1
       
 
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

