import sys
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())

for each_tuple in combinations([1,2,5,6],2):
    print(' '.join(map(str, each_tuple)))