# 문제: 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램

import sys
# 상근이가 가지고 있는 숫자 카드
user_num = int(sys.stdin.readline())
user_card = list(map(int, sys.stdin.readline().split()))

# 상근이가 가지고 있지 않은 숫자 카드
other_num = int(sys.stdin.readline())
other_card = list(map(int, sys.stdin.readline().split()))

for i in range(other_num):
    if other_card[i] in user_card:
        print(1, end=' ')
    else: 
        print(0, end=' ')