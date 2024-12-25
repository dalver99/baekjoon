import sys
from collections import deque

input = sys.stdin.readline

def bfs(V):
    global wall_map
    q = deque()
    q.append(V)

    while q:
        current = q.popleft
        x = current[0]
        y = current[1]
        crash = current[2]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in moves:
            nx = x+dx
            ny = y+dy
            #벽을 부술 수 없는 경우
            if (0 <= nx) and (nx < M) and (0<= ny) and (ny<M) and wall_map[ny][nx] == 0:
                q.append((nx,ny))
        
            #벽을 부술 수 있는 경우
                #벽을 부순 경우
                #벽을 부수지 않은 경우



wall_map = []
N,M = map(int,input().split())
for _ in range(N):
    row = list(map(str,input().strip()))
    wall_map.append(row)

#print(wall_map)

bfs((0,0,1)) # 0,0에서 시작, 1은 아직 벽을 부술 수 있음