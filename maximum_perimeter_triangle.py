#!/bin/python3

import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
    index = n - 3
    while index >= 0 and (sticks[index] + sticks[index+1] <= sticks[index+2]):
        index -= 1
    if index >= 0:
        print(sticks[index], sticks[index+1], sticks[index+2])
    else:
        print(-1)

n = int(input())

sticks = sorted(int(i) for i in input().split())

maximumPerimeterTriangle(sticks)


