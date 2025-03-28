import sys
input = sys.stdin.readline
N = int(input())
nums = []
for _  in range (N):
    nums.append(list(map(int,input().split())))

#print(nums)

#MAX
# dp_max_now = [] #n번쨰 행에 도착했을때, 최대점수를 기록
# dp_max_future = [0,0,0]
# dp_max_now = nums[0]

# for i in range (1,N):
#     dp_max_future[0] = max(nums[i][0]+dp_max_now[0],nums[i][0]+dp_max_now[1])
#     dp_max_future[1] = max(nums[i][1]+dp_max_now[0],nums[i][1]+dp_max_now[1],nums[i][1]+dp_max_now[2])
#     dp_max_future[2] = max(nums[i][2]+dp_max_now[2],nums[i][2]+dp_max_now[1])
#     print(dp_max_future)
#     dp_max_now = dp_max_future

dp = [[0]*3 for _ in range(N)]
dp[0] = nums[0]

for i in range (1,N):
    dp[i][0] = max(nums[i][0]+dp[i-1][0],nums[i][0]+dp[i-1][1])
    dp[i][1] = max(nums[i][1]+dp[i-1][0],nums[i][1]+dp[i-1][1],nums[i][1]+dp[i-1][2])
    dp[i][2] = max(nums[i][2]+dp[i-1][1],nums[i][2]+dp[i-1][2])
M = max(dp[i])
#MIN

dp = [[0]*3 for _ in range(N)]
dp[0] = nums[0]

for i in range (1,N):
    dp[i][0] = min(nums[i][0]+dp[i-1][0],nums[i][0]+dp[i-1][1])
    dp[i][1] = min(nums[i][1]+dp[i-1][0],nums[i][1]+dp[i-1][1],nums[i][1]+dp[i-1][2])
    dp[i][2] = min(nums[i][2]+dp[i-1][1],nums[i][2]+dp[i-1][2])
print(M, min(dp[i]))
