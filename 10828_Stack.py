"""
백준 문제 번호: 10828
문제 이름: 스택
난이도: Silver IV
알고리즘: Stack
"""

## ❌ 시간초과 풀이 ##
## 원인 : 입출력 I/O 문제
# stack = []
# num = int(input())

# for i in range(num):
#     cmd = input().split()
#     if cmd[0] == "push" :
#         stack.append(int(cmd[1]))
#     elif cmd[0] == "top":
#         if stack:
#             print(stack[-1])
#         else: 
#             print(-1)
#     elif cmd[0] =="size":
#         print(len(stack))
#     elif cmd[0] =="empty":
#         if stack :
#             print(0)
#         else: 
#             print(1)
#     elif cmd[0] == "pop":
#         if stack :
#             print(stack.pop())
#         else:
#             print(-1)

## 개선 풀이 
import sys

stack = []
num =int(sys.stdin.readline())

for i in range(num):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push" :
        stack.append(int(cmd[1]))
    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else: 
            print(-1)
    elif cmd[0] =="size":
        print(len(stack))
    elif cmd[0] =="empty":
        if stack :
            print(0)
        else: 
            print(1)
    elif cmd[0] == "pop":
        if stack :
            print(stack.pop())
        else:
            print(-1)