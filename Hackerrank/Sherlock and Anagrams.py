#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    # 부분 문자열의 경우의 수를 전부 구한 후, 이를 sorting 하여 dictionry 에 '문자열':'수' 로 넣음
    count = {}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            temp_list = sorted(s[i:j])
            temp_string = ''
            for k in range(len(temp_list)):
                temp_string+=temp_list[k]
            if temp_string in count:
                count[temp_string] = count[temp_string]+1
            else:
                count[temp_string] = 1
    
    # nC2 를 하게 되면, 선택할 수 있는 페어쌍의 수를 구할 수 있음 -> 전체 합을 구함
    total = 0
    for i in count.values():
        total += i*(i-1)/2*1
    
    return int(total)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
