#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    if __name__ == '__main__':
        arr = []

        for _ in range(6):
            arr.append(list(map(int, input().rstrip().split())))
        sum = 0
        larr = []

        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if k == i + 1 and (l == j or l == j + 2):
                            continue
                        else:
                            sum += arr[k][l]
                larr.append(sum)
                sum = 0

        print(max(larr))
