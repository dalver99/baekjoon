from collections import deque
import sys

def bfs(y, x):
    q = deque([(y, x)]) 
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1 and dist[ny][nx] == -1:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1


N,M = map(int,sys.stdin.readline().split())

dist = [[-1]*(M) for _ in range (N)]
matrix = []

for y in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)
    if 2 in row:
        x = row.index(2)
        start_y, start_x = y, x
        dist[start_y][start_x] = 0  # Distance to the goal is 0

bfs(start_y, start_x)

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 0:
            print(0, end=' ')
        else:
            print(dist[y][x], end=' ')
    print()