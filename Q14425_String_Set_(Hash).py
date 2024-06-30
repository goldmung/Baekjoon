# 총 N개의 문자열로 이뤄진 집합 S , M개의 문자열 중에서 집합 S에 포함되어 있는게 몇개 인지 구하기
# Hash Algorithm을 이용한 경우
# 파이썬에서는 set과 dictionary가 hash table을 활용하기 때문에 list에 비해 속도가 빠름

import sys
N,M = map(int, sys.stdin.readline().split())

S = dict()
count = 0
for _ in range(N):
    temp = sys.stdin.readline()
    S[temp] = True

for _ in range(M):
    temp = sys.stdin.readline()
    if temp in S.keys():
        count +=1

print(count)