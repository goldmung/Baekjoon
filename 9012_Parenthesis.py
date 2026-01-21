'''
알고리즘 : 스택
'''
import sys

T = int(sys.stdin.readline())

for i in range(T):
    ps = list(sys.stdin.readline().rstrip())
    temp = []
    result = ''
    for j in ps:
        if j == '(' :
            temp.append('(')
        else:
            if not temp: 
                result = "NO"
                break;
            else:
                temp.pop()
    if temp or result == "NO":
        print("NO")
    else:
        print("YES")