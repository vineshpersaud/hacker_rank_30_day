import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
#convert to binary then to string
binary = str(format(n,"b"))

#splits the binary number on 0 then finds max 1s and then length
print (len(max(binary.split("0"))))
