#풀이법이 살짝은 기억이 나는데 .. 
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

stuff = []
for _ in range (N):
    w,v = map(int,input().split())
    stuff.append((w,v))

dp = [[0] * (K+1) for _ in range (N+1)]
#dp[y][x] = y번째 아이템까지 고려시, 무게 x일 때 최대가치
#안에 값으로는 그 당시의 총 가치를 넣어보자.

for i in range(1, N + 1): #아이텡믈 하나씩 고려하며,
    w, v = stuff[i - 1] 
    for j in range(K + 1):
        if j < w:
            #현재 무게 j에 절대 못담는 경우
            dp[i][j] = dp[i - 1][j]
        else:
            #그냥 가는 경우 vs 담는 경우 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])

#나중에 니힘으로 풀어서 내라
