import sys
case = int(sys.stdin.readline().rstrip())

for _ in range(case):
    wears = int(sys.stdin.readline().rstrip())
    if wears == 0:
        print('0')
    else:
        types = []
        nums = []
        for _ in range (wears):
            name, type = sys.stdin.readline().rstrip().split()
            if types.count(type) == 0:
                types.append(type)
                nums.append(1)
            else:
                nums[types.index(type)] += 1
        howmany = 1
        for nonaked in nums:
            howmany *= (nonaked+1)
        print(howmany-1)