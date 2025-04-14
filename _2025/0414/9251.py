first = input() # ABCDA 첫단어를 세로에
second = input() # AECEDA 두번쨰 단어를 가로에 두갔어

dp = [[0]*(len(second)+1) for _ in range((len(first)+1))]

for i in range (1,len(first)+1):
    for j in range (1,len(second)+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])

#코테전에 다시..
#DP가 아직 너무너무 약함..