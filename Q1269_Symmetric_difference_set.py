import sys

# 집합 A, B의 원소 개수 입력
A, B = map(int, sys.stdin.readline().split())

# 집합 A의 원소
A_set = set(sys.stdin.readline().split())
# 집합 B의 원소
B_set = set(sys.stdin.readline().split())

# A-B 개수 구하기
cnt_AB = len(A_set - B_set)
# B-A 개수 구하기
cnt_BA = len(B_set - A_set)

print(cnt_AB + cnt_BA)