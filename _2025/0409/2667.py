import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range (N):
    graph.append(list(input().strip()))

visited = [[0]*N for _ in range(N)]

#print(graph)

#dfs로도 해보는 건 어때 이새끼야
def bfs(v):
    pops = 0
    q = deque()
    q.append(v)
    color = graph[v[0]][v[1]]
    visited[v[0]][v[1]] = 1
    while q:
        now = q.popleft()
        pops += 1
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        for dy,dx in moves:
            ny = dy+now[0]
            nx = dx+now[1]
            if 0<= nx <N and 0<=ny<N and graph[ny][nx] == color and not visited[ny][nx]:
                q.append([ny,nx])
                visited[ny][nx] = 1
    return pops

allcount = []
for i in range (N):
    for j in range(N):
        if not visited[i][j] and int(graph[i][j]):
            # print(i,j)
            count = bfs([i,j])
            allcount.append(count)

print(len(allcount))
sortedcount = sorted(allcount,key=lambda x: x)
for element in sortedcount:
    print(element)
# print(sortedcount)
