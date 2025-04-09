import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range (N+1)]
for _ in range (M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bacon(v):
    q = deque()
    visited = [0] * (N+1)
    bacon = [999] * (N+1)
    bacon[v] = 0
    bacon[0] = 0

    q.append([v,0]) #q에는 친구까지의 거리를 기재
    while q:
        now, dist = q.popleft()
        for friend in graph[now]:
            if not visited[friend]:
                visited[friend] = 1
                bacon[friend] = dist + 1
                q.append([friend,dist+1])

    return bacon

allcons = []
for i in range (1,N+1):
    allcons.append(sum(bacon(i)))

print(allcons.index(min(allcons))+1)

##BFS는 어려워
#코테보기 전에 복습
