from collections import deque

def bfs(x,y):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    for moves in move:
        dx,dy = moves
        nx = x+dx
        ny = y+dy
        if 0<=nx<M and 0<=ny<N and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            q.append([nx,ny])


M,N = map(int,input().split())
box = []
q = deque()

for n in range (N):
    line = list(map(int,input().split()))
    box.append(line)
    for m in range(M):
        if line[m] == 1:
            q.append([m,n]) # x,y 

while q:
    cur = q.popleft()
    x = cur[0]
    y = cur[1]
    bfs(x,y)

maxi = 0
for m in range(M):
    for n in range(N):
        if box[n][m] == 0:
            maxi = -1
        if maxi != -1:
            maxi = max(maxi,box[n][m])

if maxi==-1:
    print(-1)
else:
    print(maxi-1)