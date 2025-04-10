import heapq, sys
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(q,-x)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)