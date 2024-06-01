arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 카운트할 배열 = 인덱스 수 설정
cnt=[0]* (max(arr)+1)

# 각 데이터에 해당하는 인덱스 값 +1을 한다
for i in range(len(arr)):
	cnt[arr[i]] +=1

for i in range(len(cnt)):
	#  cnt의 인덱스 하나를 돈다
	for _ in range(cnt[i]):
		# i를 cnt의 값만큼 반복출력하고 빠져나와서 다음 인덱스로 이동
		print(i, end =' ')