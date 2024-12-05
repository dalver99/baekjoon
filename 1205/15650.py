import sys
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())

for each_tuple in combinations(range(1,N+1),M):
    print(' '.join(map(str, each_tuple)))