# ax + by = c
# dx + ey = f
# 각 칸에는 -999 이상 999 이하의 정수만 입력 

a, b, c, d, e, f = map(int, input().split())

for x in range (-999, 1000):
    for y in range (-999, 1000):
        if a*x + b*y == c :
            if d*x + e*y ==f :
                print(x, y)