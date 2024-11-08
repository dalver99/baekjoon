from collections import deque
import sys

def bfs(x,y):
    q = deque([(x,y)])
    
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        x,y = q.popleft()
        for move in moves:
            dx,dy = move
            if 0 <= x+dx <= M-1 and 0 <= y+dy <= N-1 and matrix[x+dx][y+dy] == 1 and dist[x+dx][y+dy] == 0:
                q.append((x+dx,y+dy))
                dist[x+dx][y+dy] = dist[x][y]+1

N,M = map(int,sys.stdin.readline().split())

dist = [[0]*(M) for _ in range (N)]
matrix = []

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)

bfs(0,0)

#도달할 수 없는곳은 -1 출력 > dist에서 0이 찍혀있는데, matrix에서 0이 아니면 -1
for row in dist:
    for i in row:


for row in dist:
    for elem in row:
        print(elem, end=" ")
    print()
