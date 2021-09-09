#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

# 문자 2개가 주어졌을 때, 앞에서부터 몇 번째까지 같은 문자인지를 반환하는 함수 작성

def wheresame(s,t):
    index = 0
    for i in range(min(len(s),len(t))):
        if s[i] == t[i]:
            index = i
        else:
            break
    
    return index+1

def appendAndDelete(s, t, k):
    # Write your code here
    # 두 문자의 같은 지점 밖에 문자들을 지우기 위해 필요한 횟수
    check = len(s) + len(t) - wheresame(s,t) - wheresame(s,t)
    
    # check 보다 주어진 숫자가 크면서 2의 배수인 경우이면 가능
    # 2의 배수인 이유는 지우고 다시 써야하기 때문에
    # 혹은 두 문자열의 길이보다 크면 전체를 다 지우고 쓸수 있기 떄문에 2의 배수일 필요가 없음
    
    if (check<=k and (check-k)%2==0) or k >= len(s)+len(t):
        return "Yes"
    
    return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
