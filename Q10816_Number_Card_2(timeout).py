# 상근이는 N개의 카드를 가짐, 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하기

import sys

# 상근이 가지고 있는 숫자 카드의 수 N
N = int(sys.stdin.readline())
# 상근's 카드에 적혀 있는 정수
N_list = list(map(int,sys.stdin.readline().split()))

# 다른 카드 수, 카드에 적힌 숫자
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

## 상근이가 몇개를 가지고 있는지 구하기
count = 0
count_list = []
for i in M_list:
    for j in N_list:
        if i==j :
            count +=1
    count_list.append(count)
    count = 0

for i in count_list:
    print(i, end=' ')