#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    bin_n = bin(n)[2:]
    print(len(max(bin_n.replace('0', ' ').split(), key=len)))

