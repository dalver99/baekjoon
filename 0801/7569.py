from collections import deque 

def bfs(x,y,z):
    move = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    for dz,dy,dx in move:
        nz,ny,nx = z+dz,y+dy,x+dx
        if 0<=nx<M and 0<=ny<N and 0<=nz<H and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] +1
            q.append([nz,ny,nx])


M,N,H = map(int,input().split())

# box = [[[0]*M for _ in range (N)] for _ in range (H)]
box = []
q = deque()

for h in range(H):
    layer = []
    for n in range(N):
        xline = list(map(int, input().split()))
        layer.append(xline)
        for m in range(M):
            if xline[m] == 1:
                q.append((h, n, m))
    box.append(layer)

while q:
    cur = q.popleft()
    x = cur[2]
    y = cur[1]
    z = cur[0]
    bfs(x,y,z)

max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:  
                print(-1)
                exit()
            max_days = max(max_days, box[h][n][m])

print(max_days - 1)  