# 문자열 S가 주어졌을 때, S의 서로 다른 문자열의 개수를 구하는 프로그램

import sys
# 문자열 S 입력
S = str(sys.stdin.readline())

S_list = []
# 서로 다른 문자열 n개씩 출력
for n in range(1,len(S)):
    for i in range(len(S)-1):
        S_list.append(S[i:i+n])

# 리스트에서 줄바꿈 문자 ('\n') 포함되지 않는 문자열만 새 리스트로 생성
S_list = [temp for temp in S_list if '\n' not in temp]
# 중복 제거
S_list = set(S_list)

# 개수 출력
print(len(S_list))