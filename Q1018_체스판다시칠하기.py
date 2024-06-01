# M*N 크기의 보드 , 각각의 칸은 검은색과 흰색으로 나눠져서 칠해져있음
# 변을 공유하는 두개의 사각형은 다른 색으로 칠해져 있어야 함
# 체스판을 칠하는 경우는 2가지 - 맨 왼쪽 위 칸이 흰색인 경우, 검은색인 경우

import numpy as np

# 체스판 크기 지정
N, M = map(int, input().split())

# 현재 칠해진 체스판 상태
pre_chess = []
for i in range(N):
    temp= list(map(str, input()))
    pre_chess.append(temp)

# # 8*8 형태의 체스판 추출
count = 0
count_list = []

for i in range(N-8+1):
     for j in range(M-8+1):
        result_chess=[]
        for row in pre_chess[i:i+8]:
            sliced_chess= row[j:j+8]
            result_chess.append(sliced_chess)
        print(np.stack(np.array(result_chess), axis=1))

        if result_chess[0][0]=='B':
            