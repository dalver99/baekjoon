import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = []

for _ in range (N):
    row = list(input().strip())
    grid.append(row)

visited = [[False]*N for _ in range (N)]
rgbcount = [0,0,0]

gridcolorblind = [[ "G" if cell == "R" else cell for cell in row ] for row in grid]
visitedcolorblind = [[False]*N for _ in range (N)]
colorblindrgbcount = [0,0] #RG, B

# print(grid)
# 여기서는 RGB를 다 따로 취급해보자.
def bfs(point):
    y,x = point[0],point[1]
    q = deque()
    q.append([y,x])
    whatcolor = grid[y][x]
    #print(whatcolor)

    while q:
        curry,currx = q.popleft()
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        for dx,dy in moves:
            if curry + dy >= 0 and curry + dy < N and currx + dx >= 0 and currx + dx < N and visited[curry + dy][currx+dx] == False and whatcolor == grid[curry+dy][currx+dx]:
                visited[curry+dy][currx+dx] = True
                q.append([curry+dy,currx+dx])

#모든점에 대해 BFS 수행. 근데 B면 안함. 그리고 원본 그래프를 바꿔버림.
count = 0
for i in range (N):
    for j in range (N):
        if not visited[i][j]:
            bfs([i,j])
            count += 1

#print(rgbcount)

def cbbfs(point):
    y,x = point[0],point[1]
    q = deque()
    q.append([y,x])
    whatcolor = gridcolorblind[y][x]
    #print(whatcolor)


    while q:
        curry,currx = q.popleft()
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        for dx,dy in moves:
            if curry + dy >= 0 and curry + dy < N and currx + dx >= 0 and currx + dx < N and visitedcolorblind[curry + dy][currx+dx] == False and whatcolor == gridcolorblind[curry+dy][currx+dx]:
                visitedcolorblind[curry+dy][currx+dx] = True
                q.append([curry+dy,currx+dx])

#모든점에 대해 BFS 수행. 근데 B면 안함. 그리고 원본 그래프를 바꿔버림.
cbcount = 0
for i in range (N):
    for j in range (N):
        if not visitedcolorblind[i][j]:
            cbbfs([i,j])
            cbcount += 1

#print(colorblindrgbcount)

print(count, cbcount)