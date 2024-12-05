import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
# 2차원 리스트에 트리 저장(연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

print(tree)

def BFS(start):
    q = deque()
    q.append((start,0))
    visited = [0] * (V+1)
    visited[start] = 1
    far = [0,0]

    while q:
        point, dist = q.popleft()
        for adj_node, adj_dist in tree[point]:
            if visited[adj_node] == 0:
                cal_dist = dist + adj_dist
                q.append((adj_node,cal_dist))
                visited[adj_node] = cal_dist
                if far[1] < cal_dist:
                    far[0] = adj_node
                    far[1] = cal_dist
    return far


point, _ = BFS(1)
print(BFS(point)[1])   