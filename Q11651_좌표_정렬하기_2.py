# 문제: 2차원 평면 위의 점 N개, 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력

import sys

spot = int(sys.stdin.readline())
coordinate = [list(map(int,sys.stdin.readline().split())) for _ in range(spot)]

#y좌표- x좌표를 기준으로 정렬하기
coordinate.sort(key=lambda x: (x[1], x[0]))

for i in range(spot):
    print(coordinate[i][0], coordinate[i][1])