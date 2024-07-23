M,N,H = map(int,input().split())

box = [[[0]*M for _ in range (N)] for _ in range (H)]

def bfs():
    pass

#3차원 BFS..
#[[[0], [0]], [[0], [0]], [[0], [0]], [[0], [0]]]

for i in range (M):
    for j in range (N):
        for k in range (H):
            bfs(i,j,k)
