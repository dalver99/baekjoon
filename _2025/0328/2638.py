""""
입력을 받고
치즈가 없는 공간을 0,0부터 BFS해서 2로 바꿈
이제 이터레이션마다 각 치즈마다 2랑 닿은게 두개면 2로 바꿈
그러고나서 새로 노출된 내부공간이 있을 수 있으니 0,0부터 BFS로 해서 0을 2로 다 바꿈
"""
import sys
from collections import deque 
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
for _ in range (N):
    row = list(map(int,input().split()))
    graph.append(row)

#print(graph)

def BFS_OUTSIDE(V):
    q = deque()
    q.append(V)
    graph[0][0] = 2
    while q:
        y,x = q.popleft()
        #3,1이면 1이 나오겠지 graph[y][x]로
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for (dx, dy) in moves:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
                graph[ny][nx] = 2 #2는 찐외부, #1은 치즈. ㅇㅋ?
                q.append((ny,nx))

#이제 0은 아직 체크 안한 내부 공간, 

count = 0
BFS_OUTSIDE((0,0)) #0,0부터 진짜 외부를 확정하고
while any(1 in row for row in graph):
    new_graph = copy.deepcopy(graph)
#    print("copied")
    for y in range (N):
        for x in range (M): #모든 칸을 돌며
            if graph[y][x] == 1: #너 치즈야?
#                print(f'for square{x},{y}')
                adj = 0
                moves = [(0,1),(0,-1),(1,0),(-1,0)]
                for (dx, dy) in moves:
                    nx = x+dx
                    ny = y+dy
                    if graph[ny][nx] == 2:
#                        print(f'sqaure {nx},{ny} is outside!')
                        adj += 1
                if adj >= 2: #인접 두칸이상이 바깥이면
                    new_graph[y][x] = 2 #2로 변경!
    BFS_OUTSIDE((0,0))
    graph = new_graph
#    print(graph)
    count += 1
print(count)
