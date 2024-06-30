# 총 N개의 문자열로 이뤄진 집합 S , M개의 문자열 중에서 집합 S에 포함되어 있는게 몇개 인지 구하기
# 일반적으로 list를 사용해 한 경우
import sys
N, M= map(int, input().split())

# N개의 문자열 입력
N_list = [(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
# M개의 문자열 입력
M_list = [(sys.stdin.readline().rstrip('\n')) for _ in range(M)]

count = 0
for i in M_list:
    if i in N_list:
        count += 1

print(count)