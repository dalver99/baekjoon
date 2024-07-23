n = int(input())

for _ in range(n):
    x,y,b = map(int,input().split())
    farm = [[0]*x for _ in range(y)]
    visited = [[0]*x for _ in range(y)]
    q = []
    for _ in range(b):
        bx,by = map(int,input().split()) 
        q.append([bx,by])
        farm[bx][by] = 1 #이거 필요하긴함?

    cur = q.pop(0)
    moves = [[0,1],[0,-1],[-1,0],[1,0]]
    while q:
        miniq = q
        visited = []
        while miniq:
            x,y = miniq.pop(0)
            visited[x][y] == 1
            for dx,dy in moves:
                nx = x + dx
                ny = y + dy
                if 0<=ny<y and 0<=nx<x and visited[nx][ny] == 0 and 
                


                
        #배추위치 '하나' 잡아서
        #주변을 돌면서 모아뒀다가
        #한방에 큐에서 제거
        #벌레 + 1
    