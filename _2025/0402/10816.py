import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
fromlist = list(map(int,input().split()))
M = int(input())
findlist = list(map(int,input().split()))

count_dict = Counter(fromlist)
countlist = [count_dict[this] for this in findlist]
print(*countlist)

#시간복잡도 및 기술면접대비할 수 있는 내용이 알차게 있다.