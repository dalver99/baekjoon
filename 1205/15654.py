import sys
from itertools import permutations
N,M = map(int,sys.stdin.readline().split())
leest = list(map(int,sys.stdin.readline().split()))
leest.sort()
for each_tuple in permutations(leest,M):
    print(' '.join(map(str, each_tuple)))