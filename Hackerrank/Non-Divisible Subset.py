#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    # 2 숫자(a,b)의 합을 k로 나눈 나머지가 0 이 되는 케이스
    # a 를 k 로 나눈 나머지와 b 를 k 로 나눈 나머지를 더했을 때 0 이거나 k 일 경우
    # 배열의 각 수를 k로 나눈 나머지를 계산하여 그 수를 저장
    # 3 가지 경우의 수로 나눔
    
    index = []
    
    for i in range(k):
        index.append(0)
    
    for i in s:
        temp = i % k
        index[temp] += 1
    
    # 첫번 째 경우의 수, 나머지가 0인 수는 1개 이하로만 들어와야함
    count = min(index[0],1)
    
    # 두번 째 경우의 수, 나머지가 k 가 짝수이면서 중간일 경우는 1 개 이하로만 들어가야함
    # 예를들어, 4 이면 나머지가 2인 숫자는 0개 or 1개만 들어와야함
    if k % 2 == 0:
        count += min(index[k//2],1)
    
    # 세번 째 경우의 수, 나머지가 i 인 수와 k-i 인 수 둘 중에 한 묶음만 들어와야 함
    for i in range(1,(k//2)+1):
        if i != k-i:
          count += max(index[i], index[k-i])
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
