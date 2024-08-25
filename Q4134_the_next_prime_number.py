# 정수 n이 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수를 찾는 프로그램

import sys
import math

# TC 입력
TC = int(sys.stdin.readline())

# 숫자 입력
num_list = [int(sys.stdin.readline().strip()) for _ in range(TC)]

# 소수 판별하는 함수
def is_prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True

# num 보다 크거나 같은 소수 중 가장 작은 소수 구하기
for i in num_list:
    while True:
        if is_prime_num(i)==1:
            print(i)
            break;
        else:
            i =i+1