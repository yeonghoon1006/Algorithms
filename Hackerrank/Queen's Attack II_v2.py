#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    # obstacles 를 튜플화하고 다시 set 화
    to_set=set([tuple(i) for i in obstacles])
    
    # 위,아래,대각선 방향 설정
    direct=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    count=0
    # 방향성 기준으로 잡고 while로 확산하다 to_set 안에 있으면 stop 하고 다음 방향 계산
    for x,y in direct:
        cur=(r_q+x,c_q+y)
        while 1<=cur[0]<=n and 1<=cur[1]<=n and cur not in to_set:
            cur=(cur[0]+x,cur[1]+y)
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
