import sys, heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())

graph = [[] for _ in range (N+1)]

for _ in range (M):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))
#print(graph)

INF = int(1e5)
dist_table = [INF] * (N+1)


def dijkstra(V):
    q = []
    heapq.heappush(q,(V,0))
    dist_table[V] = 0

    while q:
        current,dist = heapq.heappop(q)
        if dist > dist_table[current]:
            continue

        for end,roaddist in graph[current]:
            new_dist = dist + roaddist
            if new_dist < dist_table[end]:
                dist_table[end] = new_dist
                heapq.heappush(q,(end, new_dist))

dijkstra(X)
answer = dist_table[:]
#print(answer)
            
dist_table = [INF] * (N+1)

for i in range(1,N+1):
    if i!=X:
        dijkstra(i)
        answer[i] += dist_table[X]
        dist_table = [INF] * (N+1)

print(max(answer[1:]))

        
