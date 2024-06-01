# 문제: 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬

import sys

# 정렬하려고 하는 수 num 입력, 단 리스트에 하나씩 입력될 수 있도록 설정
num = list(map(int, sys.stdin.readline().rstrip()))

# 내림차순으로 정렬하기
num.sort(reverse=True)

# join함수 사용해 리스트 다시 한 숫자처럼 만들기 
# join은 str이 들어가야하기 때문에 str로 변경 후 다시 int로 변경하는 작업 수행
join_num = int("".join(map(str,num)))

print(join_num)