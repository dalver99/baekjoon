_,M = map(int,input().split())
nums = sorted(list(map(int,input().split())))
from itertools import combinations_with_replacement
combs = combinations_with_replacement(nums,M)

unique_combs = sorted(set(combs))

for comb in unique_combs:
    print(*comb)