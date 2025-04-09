import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range (N):
    graph.append(list(map(int,input().split())))

#print(graph)

ans = []

def bfs(v):
    q = deque()
    visited = [0] * N
    q.append(v)
    while q:
        now = q.popleft()        
        for idx, able in enumerate(graph[now]):
            if able == 1 and not visited[idx]:
                q.append(idx)
                visited[idx] = 1

    return visited

for dots in range(N):
    #내는 모르겠고 점은 0부터 N-1임. ㅇㅋ?
    #각 점으로부터 갈 수 있는지를 체크해서, 그걸로 새로운 걸 출력하갔어
    print(*bfs(dots))
