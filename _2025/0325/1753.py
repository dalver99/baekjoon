import sys, heapq

input = sys.stdin.readline

V,E = map(int,input().split())

K = int(input())

graph = [[] for _ in range (V+1)]

for _ in range (E):
    start, end, weight = map(int,input().split())
    graph[start].append((weight,end))

#print(graph)

INF = int(1e9)
dist_table = [INF] * (V+1)

def dijkstra(X):
    q = []
    heapq.heappush(q,(0,X))
    dist_table[X] = 0

    while q:
        current_weight, current = heapq.heappop(q)
        if dist_table[current] < current_weight:
            continue

        for next_weight, next_point in graph[current]:
            new_weight = next_weight + current_weight
            if new_weight < dist_table[next_point]:
                dist_table[next_point] = new_weight
                heapq.heappush(q,(new_weight,next_point))

dijkstra(K)
#print(dist_table)
for i in range(1,len(dist_table)):
    print(dist_table[i] if dist_table[i] != INF else "INF")
    