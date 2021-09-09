#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i])
        
    for i in range(1,len(arr2)):
        arr2[i] = max(arr2[i],arr2[i-1]+arr2[i])
         
    total1 = max(arr2)
        
    total2 = 0
    for i in range(len(arr)):
        if arr[i]>0:
            total2 += arr[i]
    
    if total2 == 0:
        total2 = max(arr)  
    
    return total1,total2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
