# 종말의 수 = 6이 적어도 3개 이상 연속으로 들어가는 수
# 첫번째 = 666, 두번째 = 1666 ...
# 666이 연속으로 들어가는 수 중에서 n 번째의 수의 값을 출력

from itertools import product

N = int(input())

num = [0,1,2,3,4,5,6,7,8,9]
for i in product(num, '666'):
    print(i)