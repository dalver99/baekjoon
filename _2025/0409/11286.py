import sys,heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num:
        buho = num // (abs(num))
        heapq.heappush(hq,(abs(num),buho))
    else:
        if hq:
            num,buho = heapq.heappop(hq)
            print(num*buho)
        else:
            print(0)