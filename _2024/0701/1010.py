import math
import sys
i = int(sys.stdin.readline())

for _ in range(i):
    n, m = map(int,input().split())
    print (math.comb(m,n))