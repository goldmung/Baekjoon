#문제: 알파벳 소문자로 이뤄진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전순으로

import sys

N = int(sys.stdin.readline())

# 단어 입력 받기
word_list = [str(sys.stdin.readline().rstrip()) for _ in range(N)]
#중복제거
word_list = list(set(word_list))
# 길이 - 사전 순으로 정렬
word_list.sort(key=lambda x: (len(x), x))

# 한줄씩 출력
for i in range(len(word_list)):
    print(word_list[i])