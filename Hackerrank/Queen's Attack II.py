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

# x,y 가 obstacles 의 위치 중 하나인지 판단하는 함수
def check(x,y,obstacles):
    for i in range(len(obstacles)):
        if x == (obstacles[i][0]-1) and y == (obstacles[i][1]-1):
            return True
    return False

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    
    answer=0
    
    # 위,아래,대각선 모든 케이스에 따라 한 칸씩 증가시키면서 check 되면 break 
    
    # up
    temp = r_q
    while temp < n:
        temp +=1
        if check(temp-1,c_q-1,obstacles):
            break
        else:
            answer+=1
    
    # down
    temp = r_q
    while temp > 1:
        temp -=1
        if check(temp-1,c_q-1,obstacles):
            break
        else:
            answer+=1    
    
    # right
    temp = c_q
    while temp < n:
        temp +=1
        if check(r_q-1,temp-1,obstacles):
            break
        else:
            answer+=1  

    # left
    temp = c_q
    while temp > 1:
        temp -=1
        if check(r_q-1,temp-1,obstacles):
            break
        else:
            answer+=1

    # right-up
    temp1 = r_q
    temp2 = c_q
    while temp1 < n and temp2 < n:
        temp1 +=1
        temp2 +=1
        if check(temp1-1,temp2-1,obstacles):
            break
        else:
            answer+=1    

    # right-down
    temp1 = r_q
    temp2 = c_q
    while temp1 >1 and temp2 <n:
        temp1 -=1
        temp2 +=1
        if check(temp1-1,temp2-1,obstacles):
            break
        else:
            answer+=1

    # left-up
    temp1 = r_q
    temp2 = c_q
    while temp1 <n and temp2 >1:
        temp1 +=1
        temp2 -=1
        if check(temp1-1,temp2-1,obstacles):
            break
        else:
            answer+=1    

    # left-down
    temp1 = r_q
    temp2 = c_q
    while temp1 >1 and temp2 >1:
        temp1 -=1
        temp2 -=1
        if check(temp1-1,temp2-1,obstacles):
            break
        else:
            answer+=1
    
    return answer
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
