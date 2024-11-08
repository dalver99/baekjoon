import sys

one = sys.stdin.readline().rstrip()
N,M = map(int,one.split())

two = sys.stdin.readline().rstrip()
nums = [int(v) for v in two.split()]
#print(nums)

pre_sum = [0]
temp = 0
for i in nums:
    temp += i
    pre_sum.append(temp)


for _ in range (M):
    three = sys.stdin.readline().rstrip()
    start, end = map(int,three.split())
    sys.stdout.write(str(pre_sum[end] - pre_sum[start-1]) + '\n') 