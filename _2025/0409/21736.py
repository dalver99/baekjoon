import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []
for i in range(N):
    row = list(input().strip())
    graph.append(row)
    if "I" in row:
        start = [i,row.index("I")] #y,x
 
visited = [[0]*(M)for _ in range(N)]

#print(graph)
#print(start)

#BFS
def bfs(v):
    visited[v[0]][v[1]] = 1 #y,x
    q = deque()
    q.append([v[0],v[1]])
    wannameet=0

    while q:
        y,x = q.popleft()
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        for dy,dx in moves:
            ny = dy + y
            nx = dx + x
            if 0<=ny<N and 0<=nx<M and graph[ny][nx] != "X" and not visited[ny][nx]:
                #print(ny,nx)
                if graph[ny][nx] == "P":
                    wannameet += 1
                q.append([ny,nx])
                visited[ny][nx] = 1
    if wannameet:    
        print(wannameet)
    else:
        print("TT")

bfs(start)