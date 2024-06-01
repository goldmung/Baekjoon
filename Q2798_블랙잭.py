# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대 크게 만들기

# (김정인 버전)
# 딜러 - N장의 카드를 숫자가 보이도록 바닥에 놓기
#     - 숫자 M을 외치기
# 플레이어 - 제한된 시간 안에 N장의 카드 중 3장의 카드 고르기
#        - 고른 카드의 합은 M을 넘지 않으며 M과 최대한 가깝게 만들기

from itertools import combinations

N, M = map (int, input().split())
nums = list(map(int, input().split()))

combine = combinations(nums, 3)

sums = []
for i in combine:
    sums.append(sum(i))

new_sums=[]
for i in sums:
    if i <= M :
         new_sums.append(i)

new_sums.sort()

print(new_sums[-1])