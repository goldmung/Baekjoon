# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합
# 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 함
# 예) 245의 분해합 256(=245+2+4+5) -> 245는 256의 생성자

N = int(input())

num = 0
result = 0
for num in range (N):
    sum_num = sum(map(int, list(str(num))))
    if N == num + sum_num :
        result = num
        print(result)
        break
    num += 1
if result ==0 :
    print(0)