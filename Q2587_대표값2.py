# 중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값
# 예시 : 10 30 30 40 60  -> 중앙값 : 30

# 문제: 5개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성

# 입력값을 넣어둘 리스트 선언
temp_list = []

# 1-5줄까지 한줄에 하나씩 자연수 입력
for i in range (5):
    temp= int(input())
    temp_list.append(temp)

# 오름차순으로 리스트 정렬
sorted_list = sorted(temp_list)

# 평균 구하기
sum_list = 0
for i in sorted_list:
    sum_list += i 
print(int(sum_list/5))

# 중앙값 구하기
print(sorted_list[2])