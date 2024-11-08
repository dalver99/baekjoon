N,M = map(int,input().split())

def find(a,b):
    visited = [[0]*M for _ in range (N)]
    q = [[a,b]]
    visited[a][b] = 1
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        y,x = q.pop(0)
        for dx,dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0 and graph[ny][nx] != 0:
                visited[ny][nx] = visited[y][x]+1
                q.append([ny,nx])
    #print(graph)
    #print(visited)
    
    return visited[N-1][M-1]


graph = [[0]*M for _ in range (N)]

for k in range (N):
    string = input()
    listring = list(string)
    for i in range (len(listring)):
        graph[k][i] = int(listring[i])

print(find(0,0))