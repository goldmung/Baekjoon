# 문제: N명의 학생 응시, 이들 중 가장 높은 k명은 상을 받음. 이 때, 상을 받는 커트라인이 몇 점인지 구하라

# 응시자 수  N명, 사람의 수 k가 공백을 두고 주어짐
N, k = map(int, input().split())

# 각 학생의 점수 x가 공백을 사이에 두고 입력
score_list = list(map(int, input().split()))

# 내림차순으로 정렬
score_list = sorted(score_list,reverse=True)

# 커트라인 점수 출력
print(score_list[k-1])