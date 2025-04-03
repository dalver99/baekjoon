import heapq,sys

input = sys.stdin.readline
N = int(input())

q = []
for _ in range (N):
    heapq.heappush(q,int(input()))

for _ in range (N):
    print(heapq.heappop(q))