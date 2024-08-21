import sys
from functools import reduce

# 이미 심어져 있는 가로수의 수 = N
N = int(sys.stdin.readline().strip())

# 가로수의 위치 저장
tree = []
for _ in range(N):
    temp = int(sys.stdin.readline().strip())
    tree.append(temp)

# 가로수의 간격 구하기
interval = [tree[i+1] - tree[i] for i in range (N-1)]
#print(interval)

# 가로수 간격 최대공약수 구하기
def gcd (a,b):
    while b>0:
        a, b = b, a%b
    return a

# 가로수 간격의 최대공약수를 계산하는 함수
def gcd_multiple(interval):
    return reduce(gcd,interval)

#간격 최대 공약수 구하기
result = gcd_multiple(interval)
#print(result)

# 개수 세기
count = int((tree[-1] - tree[0]) / result -N +1)
print(count)