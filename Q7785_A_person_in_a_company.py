# 로그가 주어졌을 때, 현재 회사에 잇는 모든 사람을 구하시오

import sys
n = int(sys.stdin.readline())

access_list= {}

for _ in range(n):
    commute = sys.stdin.readline().split()
    if commute[1]=='enter': 
        access_list[commute[0]] = True
    else:
        del(access_list[commute[0]])

# value 기준으로 내림차순으로 정렬
#access_list = sorted(access_list.items(), key = lambda x: x[1], reverse=True)

sorted_name = sorted(access_list.keys(), reverse=True)
for i in sorted_name:
    print(i , end = '\n')