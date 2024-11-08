def dfs(v):
    global visited, n
    visited[v] = True
    print(v, end = ' ')
    for next in range(1,n+1):
        if not visited[next] and graph[v][next]:
            dfs(next)

def bfs():
    global q, visited, n
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range (1,n+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


n,m,v = map(int,input().split())
graph =[[False]*(n+1) for _ in range (n+1)]
print(graph)

#graph = [[False] * (n+1)] * (n+1)

for _ in range (m):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

# dfs
visited = [False] * (n+1)
dfs(v)
print()


visited = [False] * (n+1)
# bfs
q = [v]
visited[v] = True
bfs()