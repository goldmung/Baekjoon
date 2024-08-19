import sys
from fractions import Fraction

# 분수 A/B 입력, C/D 입력
A,B = map(int, sys.stdin.readline().split())
C,D = map(int, sys.stdin.readline().split())

# 분수
f_ab = Fraction(A,B)
f_cd = Fraction(C,D)

# 분수 합
sum_f = f_ab+ f_cd

print(sum_f.numerator, sum_f.denominator)