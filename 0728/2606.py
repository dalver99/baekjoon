n = int(input())
con = int(input())

def bfs(v):
    global q, visited, count
    for y in range (1,n+1):
        if graph[v][y] == 1 and visited[y] == 0:
            visited[y] = 1
            #print(v,y)
            graph[v][y] = 0
            graph[y][v] = 0
            q.append(y)
            count += 1


graph = [[0] * (n+1) for _ in range (n+1)]

for _ in range(con):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#bfs for point 1
count = 0

visited = [0 for _ in range (n+1)]
q = []
bfs(1)
while q:
    #print('q'+str(q))
    point = q.pop(0)
    #print('pop'+str(point))
    bfs(point)

#print('ans'+str(count))
print(count)