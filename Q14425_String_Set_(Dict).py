# 총 N개의 문자열로 이뤄진 집합 S , M개의 문자열 중에서 집합 S에 포함되어 있는게 몇개 인지 구하기
# set, dictionary를 활용해서 한 경우

import sys
N, M= map(int, input().split())

S=[]
count = 0
# N개의 문자열 입력
for _ in range(N):
    temp = sys.stdin.readline().strip('\n')
    S.append(temp)

for _ in range(M):
    temp = sys.stdin.readline().strip('\n')
    if temp in S :
        count +=1

print(count)