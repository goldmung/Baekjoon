# 문제: Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야함

import sys
N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

# 중복 제거 & 정렬
sorted_arr = sorted(set(arr))

# X_list의 값이  sorted_list의 어느 인덱스에 위치하는 지 출력
# 처음에 index를 이용했지만 시간초과 -> 시간 복잡도 : O(n)
# dict를 이용해 시간초과 해결 -> 시간 복잡도: O(1)
dict_arr = {sorted_arr[i]: i for i in range(len(sorted_arr))}

for i in arr:
    print(dict_arr[i], end=' ')