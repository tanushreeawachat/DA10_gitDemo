#!/bin/python3

import math
import os
import random
import re
import sys

Weird = 'Weird'
notWeird = 'Not Weird'

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print(Weird)
elif n >= 2 and n <= 5:
    print(notWeird)
elif n >= 6 and n <= 20:
    print(Weird)
else:
    print(notWeird)