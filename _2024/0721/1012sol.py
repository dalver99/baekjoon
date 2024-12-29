from collections import deque

T = int(input())

def bfs(a,b):
    q = deque()
    q.append((a,b))
    move = [[1,0],[-1,0],[0,1],[0,-1]]

    while q:
        x,y = q.popleft()
        for dx,dy in move:
            nx,ny = x+dx,y+dy

            if 0<=nx<M and 0<=ny<N and farm[nx][ny] == 1:
                q.append((nx,ny))
                farm[nx][ny] = 0


for _ in range (T):
    bug = 0
    M,N,B = map(int,input().split())
    farm = [[0]*N for _ in range(M)]

    for _ in range (B):
        x,y = map(int,input().split())
        farm[x][y] = 1 # 배추가 잇어용

    for i in range (N):
        for j in range (M):
            if farm[j][i] == 1:
                bfs(j,i)
                bug +=1
    print(bug)
                


