# 포켓몬 도감 완성
# 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 방식

import sys
# 포켓몬의 개수 N, 맞춰야할 문제의 개수 M
N, M = map(int,sys.stdin.readline().split())

N_dic = {}
for i in range(N):
    pokemon_name = sys.stdin.readline().strip()
    N_dic[pokemon_name] = str(i+1)

rev_dic = {v:k for k, v in N_dic.items()}
for _ in range(M):
    temp = sys.stdin.readline().strip()
    if temp in N_dic:
        print(N_dic[temp])
    else:
        if temp in rev_dic.keys():
            print(rev_dic[temp])