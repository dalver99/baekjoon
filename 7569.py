def bfs(x,y,z):
    global visited
    visited[x][y][z] += 1
    move = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
    for dx,dy,dz in move:
        nx,ny,nz = x+dx,y+dy,z+dz
        if 0<=nx<M and 0<=ny<N and 0<=nz<H and visited[nx][ny][nz] == 0 and box[nx][ny][nz] != -1:
            visited[nx][ny][nz] = visited[x][y][z] + 1





M,N,H = map(int,input().split())



box = [[[0]*M for _ in range (N)] for _ in range (H)]

def bfs():
    pass

#3차원 BFS..
#[[[0], [0]], [[0], [0]], [[0], [0]], [[0], [0]]]

visited = [[[0]*M for _ in range (N)] for _ in range (H)]

# 1인 칸에 대해서만 해야함
bfs(i,j,k)

if visited.count():
    print(max(visited))
