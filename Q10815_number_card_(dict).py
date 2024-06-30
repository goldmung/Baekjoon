import sys
# 상근이가 가지고 있는 숫자 카드
user_num = int(sys.stdin.readline())
user_card = list(map(int, sys.stdin.readline().split()))

# 상근이가 가지고 있지 않은 숫자 카드
other_num = int(sys.stdin.readline())
other_card = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(user_num):
    dic[user_card[i]] = "1"

for i in range(other_num):
    if other_card[i] not in dic:
        print('0', end=' ')
    else:
        print('1', end = ' ')