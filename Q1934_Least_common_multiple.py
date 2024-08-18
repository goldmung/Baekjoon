import sys

# 테스트 케이스 개수
TC = int(sys.stdin.readline())

# 최대공약수
def gcd (a, b):
    while b> 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b / gcd(a,b)

# 두 자연수 A, B 입력 & A와 B의 최소공배수
for i in range(TC):
    A, B = map(int, sys.stdin.readline().split())
    print(int(lcm(A,B)))