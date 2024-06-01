# 문제: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성

# N개의 수 지정
N = int(input())

# 리스트 선언
random_list = []

# N개의 줄에 수 입력하기
for i in range(N):
    num = int(input())
    # 입력받은 수 리스트에 집어넣기
    random_list.append(num)

# 오름차순으로 정렬하기
sorted_list = sorted(random_list)

# 오름차순으로 한 줄에 하나씩 출력
for i in sorted_list:
    print(i)

# 출제자:연재환 
# 문제: 정렬된 리스트를 한 줄로 출력 각 원소는 공백으로 구분
for i in sorted_list:
    print(i, end=' ')