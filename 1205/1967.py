import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
tree = [[] for _ in range (N+1)]

for _ in range (N-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))


def BFS(start):
    q = deque()
    q.append((start,0))
    visited = [-1] * (N+1)
    visited[start] = 0
    furthest = [0,0]

    while q:
        curr_point,curr_dist = q.popleft()
        for adj_node, adj_dist in tree[curr_point]:
            if visited[adj_node] == -1:
                calc_dist = curr_dist + adj_dist
                q.append((adj_node,calc_dist))
                visited[adj_node] = calc_dist
            if furthest[1] < calc_dist:
                furthest[0] = adj_node
                furthest[1] = calc_dist
    return furthest

point,_ = BFS(1)
print(BFS(point)[1])