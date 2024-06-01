#O-표기법(빅-오)
#O(g(n))={f(n)| 모든 n >= n0에 대해 f(n) <= c * g(n)인 야의 상수 c와 n0가 존재}
# f(n) = a0n + a1 , g(n)= n

a0, a1 = map(int, input().split())
c = int(input())
num = int(input())

# 조건 설정한 방법
# a0*n +a1 <= cn
# (c-a0)*n >= a1

if a0<=c and a0*num+a1 <= c*num :
    print(1)
else:
    print(0)