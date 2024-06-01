# 문제: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성
# 단, 계수 알고리즘을 이용해 작성

import sys

# N개의 수 입력
N = int(sys.stdin.readline())

# 카운트할 배열 = 인덱스 수 설정
cnt = [0] * 10000

# 하나의 값 입력 받고, 그걸 인덱스 값에 맞춰 cnt 수 늘려주기
for i in range(N):
    temp = int(sys.stdin.readline())
    cnt[temp-1] += 1

for i in range (10000):
    if cnt[i] != 0: 
        for _ in range (cnt[i]):
            print(i+1, end= '\n')