# 김진영이 듣도 못한 사람의 수 N, 보도 못한 사람의 명단 M

import sys

# 듣도 못한 사람의 수 = N, 보도 못한 사람의 수 = M
N, M = map(int, sys.stdin.readline().split())

# 듣도 못한 사람 명단을 set에 저장
N_set = set()
for i in range(N):
    name = sys.stdin.readline().strip()
    N_set.add(name)
#print(N_list)

# 보도 못한 사람 명단을 set에 저장
M_set = set()
for i in range(M):
    name = sys.stdin.readline().strip()
    M_set.add(name)
#print(M_list)

# 두 집합의 교집합 구하기
result_set = N_set & M_set
#print(result_set)

# 듣보잡의 수 출력
print(len(result_set))

# 듣보잡 명단 사전순으로 출력
for i in sorted(result_set):
    print(i)