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
    
    # 카데인 알고리즘 적용
    # 배열을 순서대로 진행하면서, 이전까지의 최대 부분합에 지금 현재의 값을 더해야 최대의 값이 나옴
    # 그러나, 이전 최대 부분합에 현재 값을 더한 값이 현재 값보다 작으면 현재 이후 부분합은 현재 값만 이용하는게 최대 부분합
    # arr[i] = max(arr[i], arr[i-1]+arr[i])
    
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i])
        
    for i in range(1,len(arr2)):
        arr2[i] = max(arr2[i],arr2[i-1]+arr2[i])
         
    total1 = max(arr2)
    
    # 배열의 양수를 전체 더하면 최대값, 양수가 없다면 음수 중 최대값 1개만 있는 것이 최대값
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
