_,M = map(int,input().split())
nums =list(map(int,input().split()))
from itertools import permutations

combs = permutations(nums,M)
all = []
for els in combs:
    all.append(els)
#print(all)
allset = list(set(all))
sorted_allset = sorted(allset, key=lambda x: tuple(x[i] for i in range(M)))

#print(sorted_allset)
for el in sorted_allset:
    print(*el)