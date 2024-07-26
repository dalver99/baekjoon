N = int(input())

dp = [0] * 10000001
#dp = [0] * 100

#dp[i] : 숫자 i를 만드는데 필요한 최소 연산 횟수

for i in range (2, N+1) :
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) 
    
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
#print(dp)