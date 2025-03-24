import sys, heapq
#clone coding
#https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-1238%EB%B2%88-%ED%8C%8C%ED%8B%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int,input().split())

graph = [[] for _ in range (N+1)]
distance = [INF] * (N+1)
answer = []

for _ in range (M):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))

def dijkstra(X):
    q = []
    heapq.heappush(q,(0,X))
    distance[X] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(X)
answer = distance[:]
distance = [INF] * (N + 1)
print(answer)

for i in range(1, N + 1):
    if i != X:
        dijkstra(i)
        answer[i] += distance[X]
        distance = [INF] * (N + 1)
 
print(max(answer[1:]))