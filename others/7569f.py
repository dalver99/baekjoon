import time

def bfs(x,y,z):
    global visited
    time.sleep(1)
    move = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
    for dx,dy,dz in move:
        nx,ny,nz = x+dx,y+dy,z+dz
        if 0<=nx<M and 0<=ny<N and 0<=nz<H and visited[nz][ny][nx] != 1 and box[nz][ny][nx] != -1:

            box[nz][ny][nx] = box[z][y][x] + 1
            print(box)
            visited[nz][ny][nx] = 1
            q.append([nz,ny,nx])

M,N,H = map(int,input().split())
box = [[[int(0)]*M for _ in range (N)] for _ in range (H)]
visited = [[[int(0)]*M for _ in range (N)] for _ in range (H)]
q = []

for ii in range (H):
    for jj in range (N):
        xline = input().split()
        for kk in range (M):
            box[ii][jj][kk] = xline[kk]
            if xline[kk] == '1':
                visited[ii][jj][kk] = 1
                q.append([ii,jj,kk])


#3차원 BFS..
while q:
    cur = q.pop(0)
    x,y,z = cur[2],cur[1],cur[0]
    bfs(x,y,z)

print(visited)

# if visited.count(-1) == 0:
#     print(max(visited))
# else: 
#     print(max(visited))
