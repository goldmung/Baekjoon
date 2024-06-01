#문제: 2차원 평면 위의 점 N개가 주어짐, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램 작성

import sys
# 점의 개수 
spot = int(sys.stdin.readline())

# x, y의 좌표 입력
coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(spot)]

# 오름차순으로 정렬
coordinate.sort()

# 정렬된 x,y좌표 한개씩 출력
for i in range(spot):
    print(coordinate[i][0], coordinate[i][1])