import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

# 일단 다 받고
tree = [[] for _ in range (N+1)]
for _ in range (N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
#print(tree)

#DFS로 각자의 부모를 저장
parent = [0] * (N+1)
#print(parent)

def DFS(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            DFS(i)

DFS(1)
for j in range (2,N+1):
    print(parent[j])




