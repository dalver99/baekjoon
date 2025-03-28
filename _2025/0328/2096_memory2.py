import sys
input = sys.stdin.readline
N = int(input())
nums=list(map(int,input().split()))

#MAX
dp_max_future = [0,0,0]
dp_max_now = nums
    
#MIN
dp_min_future = [0,0,0]
dp_min_now = nums

for i in range (1,N):
    nums = list(map(int,input().split()))
    dp_max_future[0] = max(nums[0]+dp_max_now[0],nums[0]+dp_max_now[1])
    dp_max_future[1] = max(nums[1]+dp_max_now[0],nums[1]+dp_max_now[1],nums[1]+dp_max_now[2])
    dp_max_future[2] = max(nums[2]+dp_max_now[2],nums[2]+dp_max_now[1])
    dp_max_now = dp_max_future[:]
    dp_min_future[0] = min(nums[0]+dp_min_now[0],nums[0]+dp_min_now[1])
    dp_min_future[1] = min(nums[1]+dp_min_now[0],nums[1]+dp_min_now[1],nums[1]+dp_min_now[2])
    dp_min_future[2] = min(nums[2]+dp_min_now[2],nums[2]+dp_min_now[1])
    dp_min_now = dp_min_future[:]

print(max(dp_max_now),min(dp_min_now))
