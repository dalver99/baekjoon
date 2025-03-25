# https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-12865%EB%B2%88-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD
# great post, btw

N,K = map(int,input().split())
things = [(0,0)]
for _ in range (N):
    w,v = map(int,input().split())
    things.append((w,v))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range (1,N+1): #for item
    w,v = things[i]
    for j in range (1,K+1): #for weight
        if j >= w: #can put in
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w] + v)
        else: #cant put!
            dp[i][j] = dp[i-1][j]
    
    # for row in dp:
    #     print(row)

    # print("*" * 20)
print(dp[K][N])