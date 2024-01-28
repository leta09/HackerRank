#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[len(s)-2:] == "AM" and s[:2] != "12":
        return s[:len(s)-2]
    if s[len(s)-2:] == "PM" and s[:2] != "12":
        conv = int(s[:2]) + 12
        return str(conv)+s[2:len(s)-2]
    if s[len(s)-2:] == "AM" and s[:2] == "12":
        conv = "00"
        return conv+s[2:len(s)-2]
    if s[len(s)-2:] == "PM" and s[:2] == "12":
        return s[:len(s)-2]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()