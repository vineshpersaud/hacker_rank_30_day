#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

reverse = []

for elem in arr :
    reverse.insert(0,str(elem))

print (" ".join(reverse))