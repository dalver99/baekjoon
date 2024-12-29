import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] =True
    for i in range(1,N+1):
        if matrix[v][i] == 1 and not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if matrix[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True

# from collections import deque
# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         v = q.popleft()
#         for i in range(1, N+1):
#             if matrix[v][i] == 1 and not visited[i]:
#                 q.append(i)
#                 visited[i] = True


N, M = map(int,input().split())

matrix = [[0]*(N+1) for _ in range (N+1)]
visited = [False] * (N+1)
#print(matrix)

for _ in range (M):
    x,y = map(int,sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1


connectedguise=0

for i in range (1,N+1):
    if not visited[i]:
        dfs(i)
        #bfs(i)
        connectedguise += 1

print(connectedguise)
