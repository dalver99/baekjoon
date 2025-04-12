N,M = map(int,input().split())

poplist = list(map(int,input().split()))
nums = [i for i in range (1,N+1)]
total = 0
for _ in range (M):
    now = poplist.pop(0)
    idx = nums.index(now)
    if idx <= len(nums)/2: #그럼 2번연산을 idx번
        total += idx
        #print(total)
        for _ in range (idx):
            temp = nums.pop(0)
            nums.append(temp)
        nums.pop(0)
        #print(nums)
    else: #반대면
        total += len(nums)-idx
        #print(total)
        for _ in range (1, len(nums)-idx):
            temp = nums.pop(-1)
            nums.insert(0,temp)
        nums.pop(-1)
        #print(nums)

print(total)

