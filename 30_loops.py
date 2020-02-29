#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

for num in range(1,11):
    #print(str(n)+" x " + str(num) + " = " + str(num * n))
    print ('{} x {} = {}'.format(n,num,num*n))