import time
n = int(input())
bug = 0

for _ in range(n):
    x,y,b = map(int,input().split())
    visited = [[0]*(x+1) for _ in range(y+1)]
    q = []
    for _ in range(b):
        bx,by = map(int,input().split()) 
        q.append([bx,by])           

    # q에는 모든 배추위치 저장

    while q:
        miniq = []
        miniset = []
        #do bfs
        ax,ay = q[0]
        miniq.append([ax,ay])
        miniset = miniq
        visited[ax+1][ay+1] == 1
        move = [[1,0],[-1,0],[0,-1],[0,1]]
        while miniset:
            print(miniset)
            ax,ay = miniset.pop(0)
            time.sleep(1)
            for dx,dy in move:
                nx = ax+dx
                ny = ay+dy
                if 0 <= nx < x and 0 <= ny < y and visited[nx+1][ny+1] == 0 and q.count([nx,ny])==1:
                    visited[nx+1][ny+1] == 1
                    miniq.append([nx,ny])
                    miniset.append([nx,ny])

        for coord in miniq:
            print(miniq)
            print(q)
            q.remove(coord)
        bug += 1
        
    print(bug)
            

    # q에서 하나 꺼내서, bfs 수행 = 인접배추밭 한 미니큐에 저장, 
    # q - 미니큐, 벌레 +1
