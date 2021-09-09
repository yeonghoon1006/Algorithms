#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    # 제곱근을 구하여 특정 정수가 아니라면 큰 쪽 정수를 특정 정수이면 해당 정수 사용
    
    if math.sqrt(len(s)) == int(math.sqrt(len(s))):
        length = int(math.sqrt(len(s)))
    else:
        length = int(math.sqrt(len(s))) + 1
    
    answer = ''
    
    # 구한 정수(n)로 나누어 나머지가 0,1,2...n 인 번째의 문자를 나열
    for i in range(length):
        for j in range(len(s)):
            if j % length == i:
                answer += s[j]
        answer += ' '
    
    return answer
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    #s = 'iffactsdontfittotheorychangethefacts'
    
    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
