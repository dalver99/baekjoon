import sys, heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    maxq = []
    minq = []
    entry_valid = {}
    id_counter = 0

    n = int(input())
    for _ in range(n):
        order, n = map(str,input().split())
        n = int(n)

        if order == "I":
            heapq.heappush(minq,(n,id_counter))
            heapq.heappush(maxq,(-n,id_counter))
            entry_valid[id_counter] = True
            id_counter += 1

        elif order == "D":
            if n == 1:  #D 1
                while maxq and not entry_valid.get(maxq[0][1], False):
                    heapq.heappop(maxq)
                if maxq:
                    _, del_id = heapq.heappop(maxq)
                    entry_valid[del_id] = False
            elif n == -1:  #D -1
                while minq and not entry_valid.get(minq[0][1], False):
                    heapq.heappop(minq)
                if minq:
                    _, del_id = heapq.heappop(minq)
                    entry_valid[del_id] = False

    while minq and not entry_valid.get(minq[0][1], False):
        heapq.heappop(minq)
    while maxq and not entry_valid.get(maxq[0][1], False):
        heapq.heappop(maxq)

    if minq and maxq:
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")