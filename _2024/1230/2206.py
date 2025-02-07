import sys
input = sys.stdin.readline
from collections import deque

def bfs(V):
    global crashed
    global matrix

    visited = [[0 for _ in range (M)] for _ in range(N)]
    q = deque()
    q.append(V)
    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        currY,currX,crash = q.popleft()

        for dx,dy in moves:
            nx = currX+dx
            ny = currY+dy

            #벽을 부술 수 없는 경우
            if crash == 0 and nx >= 0 and nx < M and ny >= 0 and ny < N and matrix[ny][nx] == 0:
                q.append(nx,ny,0)
                distance[ny][nx] = distance[currY][currX] + 1
                visited[ny][nx] = 1
            #부술 수 있고 부순 경우 #일단 다 부숴보자. 최대한 빨리 부숴보고, 다시 돌아와서 다른 벽을 부숴보고..
            elif crash == 1 and nx >= 0 and nx < M and ny >= 0 and ny < N and matrix[ny][nx] == 1 and crashed[ny][nx] == 0:
                q.append(nx,ny,0)
                distance[ny][nx] = distance[currY][currX] + 1
                visited[ny][nx] = 1
            #부술 수 있지만 벽이 아닌 경우
            elif crash == 0 and nx >= 0 and nx < M and ny >= 0 and ny < N and matrix[ny][nx] == 0:
                q.append(nx,ny,0)
                distance[ny][nx] = distance[currY][currX] + 1
                visited[ny][nx] = 1


N,M = map(int,input().split())
matrix = []
crashed = [[0 for _ in range (M)] for _ in range(N)]
distance = [[0 for _ in range (M)] for _ in range(N)]

for _ in range (N):
    row = list(map(str,input().strip()))
    matrix.append(row)

bfs((1,1,1))
print(distance[N-1][M-1])