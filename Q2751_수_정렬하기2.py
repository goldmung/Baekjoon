# 문제: N개의 수가 주어졌을때, 오름차순으로 정렬하는 프로그램 작성 
# 단, 최소 시간으로 구성

import sys

# 수의 개수 N 입력
N = int(sys.stdin.readline())

# 한줄에 한개씩 n개의 줄에 입력받기
num_list=[]
for i in range (N):
    num = int(sys.stdin.readline())
    num_list.append(num)

# 오름차순으로 정렬하기
num_list.sort()

# 한줄에 하나씩 출력하기
for i in num_list:
    print(i)