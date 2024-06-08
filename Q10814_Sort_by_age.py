# 문제: 나이를 오름차순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

import sys

# 온라인 저지 회원의 수
member = int(sys.stdin.readline())

# 각 회원의 나이와 이름 입력 
member_list =[]
for _ in range(member):
    age, name = sys.stdin.readline().split()
    member_list.append([int(age), name])

# 나이 오름차순으로 정렬
member_list.sort(key=lambda x: x[0])

# 한줄씩 출력
for i in range(member):
    print(member_list[i][0], member_list[i][1])