import sys

# 두 정수 A, B 입력
A, B = map(int, sys.stdin.readline().split())

# 최대공약수 구하기
def gcd (a,b):
    while b >0:
        a, b = b, a%b
    return a

# 최소공배수 구하기
def lcm (a,b):
    return a*b / gcd(a,b)

print(int(lcm(A,B)))