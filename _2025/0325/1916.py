import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range (N+1)]
INF = int(1e9)
dist_table = [INF] * (N+1)

for _ in range (M):
    start,end,weight = map(int,input().split())
    graph[start].append((weight,end))
    
START, END = map(int,input().split())

def dijkstra(X):
    q = []
    dist_table[X] = 0
    heapq.heappush(q,(0,X))
    
    while q:
        current_weight, current = heapq.heappop(q)
        
        if current_weight > dist_table[current]:
            continue

        for next_weight, next_point in graph[current]:
            new_weight = next_weight + current_weight
            if new_weight < dist_table[next_point]:
                dist_table[next_point] = new_weight
                heapq.heappush(q,(new_weight,next_point))

dijkstra(START)
print(dist_table[END])