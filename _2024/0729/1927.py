import sys
import heapq

n = int(sys.stdin.readline().rstrip())
heap = []

for i in range (n):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')
        
    else:
        heapq.heappush(heap,x)