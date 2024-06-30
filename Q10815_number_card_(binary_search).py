import sys
# 상근이가 가지고 있는 숫자 카드
user_num = int(sys.stdin.readline())
user_card = list(map(int, sys.stdin.readline().split()))

# 상근이가 가지고 있지 않은 숫자 카드
other_num = int(sys.stdin.readline())
other_card = list(map(int, sys.stdin.readline().split()))

#이진 탐색 = 데이터가 정렬되어 있는 배열에서 찾고자 하는 수를 찾아내는 방법
# 데이터가 정렬되어 있는 배열 (오름차순)
user_card.sort()

# 찾고자 하는 수 target 
def binary_search(array, target) :
    start = 0
    end = len(array) -1
    
    while start <= end:
        mid = (start + end)//2
        if array[mid]== target :
            return True
        elif array[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return False

for i in other_card:
    if binary_search(user_card, i) :
        print(1, end = ' ')
    else:
        print(0, end = ' ') 