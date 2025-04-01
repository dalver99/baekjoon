import sys, heapq
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range (N):
    heapq.heappush(nums,int(input()))

sorted_nums = [heapq.heappop(nums) for _ in range(N)]
sansul = sum(sorted_nums) / N
sansul = round(sansul) if sansul % 1 >= 0.5 and sansul > 0 else int(round(sansul))
chungang = sorted_nums[int(N/2)]
data = Counter(sorted_nums).most_common()
#print(data)
if len(data) > 1:
    if data[0][1] == data[1][1]:
        choibin = data[1][0]
    else:
        choibin = data[0][0]
elif N == 1:
    choibin = sorted_nums[0]
else:
    choibin = sorted_nums[0]
range = sorted_nums[-1] - sorted_nums[0]
#print(sorted_nums)
print(sansul)
print(chungang)
print(choibin)
print(range)