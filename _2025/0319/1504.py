import sys,heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range (N+1)]
INF = int(1e7)
for _ in range (E):
    start,end,weight = map(int,input().split())
    graph[start].append((end,weight))
    graph[end].append((start,weight))

v1,v2 = map(int,input().split())

#print(graph)
#print(v1,v2)

def dijkstra(V):
    dist_table =  [INF] * (N+1)
    dist_table[V] = 0
    q = []
    heapq.heappush(q,[0,V])
    while q:
        current_dist, current = heapq.heappop(q)
        if dist_table[current] < current_dist:
            continue
        
        for point,point_weight in graph[current]:
            total_weight = current_dist + point_weight
            if total_weight < dist_table[point]:
                dist_table[point] = total_weight
                heapq.heappush(q,(total_weight,point))
                
    return dist_table


from1 = dijkstra(1)
fromv1 = dijkstra(v1)
fromv2 = dijkstra(v2)

route_a = from1[v1] + fromv1[v2] + fromv2[N]
route_b = from1[v2] + fromv2[v1] + fromv1[N]

#print(route_a)
#print(route_b)

ans = min(route_a,route_b)
#print(ans)
print(ans if ans < INF else -1)