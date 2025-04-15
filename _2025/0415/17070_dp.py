#파이프의 현재 상태와 끝점만 기억하자.
import sys
input = sys.stdin.readline
N = int(input())
house = []

for _ in range (N):
    house.append(list(map(int,input().split())))

#0 = 가로, 1 = 대각, 2 = 세로 인걸로 하자고.
# pipe = (0,(1,0)) #초기상태는 무조건 이거임

dp = [[[0] * 3 for _ in range (N)] for _ in range (N)]
dp[0][1][0] = 1

for y in range (N):
    for x in range (N):
        if house[y][x] == 1:
            continue
        if x > 0:
            dp[y][x][0] += dp[y][x-1][1] + dp[y][x-1][0]
        if y > 0:
            dp[y][x][2] += dp[y-1][x][1] + dp[y-1][x][2]
        if x > 0 and y > 0:
            if house[y-1][x] != 1 and house[y][x-1] !=1:
                dp[y][x][1] += dp[y-1][x-1][1] + dp[y-1][x-1][0] + dp[y-1][x-1][2]
            
#print(dp[-1][-1])
print(sum(dp[-1][-1]))