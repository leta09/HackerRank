#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if z - abs(z-y)> z - abs(z-x):
        return "Cat B"
    if z - abs(z-y)< z - abs(z-x):
        return "Cat A"
    if abs(z-y)==abs(z-x):
        return "Mouse  C"
    
if __name__ == '__main__':
   

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)

      