'''
알고리즘 : Stack
'''

## ❌ 시간초과 풀이 ##
# import sys

# n = int(sys.stdin.readline())
# stack =[]
# next_num = 1

# for i in range(n):
#     temp = int(sys.stdin.readline().rstrip())
#     while next_num <= temp:
#         stack.append(next_num)
#         print('+')
#         next_num +=1  
#     if stack[-1] ==temp :
#         stack.pop()
#         print('-')
#     else: 
#         print("NO")
#         break;

# 문제 이해하는 데 시간 많이 소요함
# 1. 입력 값들에 대한 의미 이해
# 8/ 4 3 6 8 7 5 1 -> n=8 , 목표 수열 =4,5,6,8,7,5,1
# -> 이 숫자들은 들어오는 순서가 아니고, 만들어야하는 결과
# 2. 외부에서 push 가능한 숫자
# 1-2-3-4-5-6-7-8 순으로 
# 3. 그럼 pop한 결과대로 stack의 결과가 나와야한다는거네

## 개선 풀이 
import sys

n = int(sys.stdin.readline())
stack = []
result = []
next_num = 1

for _ in range(n):
    temp = int(sys.stdin.readline())
    while next_num <= temp:
        stack.append(next_num)
        result.append('+')
        next_num += 1
    if stack[-1] == temp:
        stack.pop()
        result.append('-')
    else:
        result = ["NO"]  ## 덮어쓰기
        break

sys.stdout.write('\n'.join(result) + '\n') ## 한번에 출력