def bfs(v):
    global visited
    visited[v] = 1
    for j in range (1,N+1):
        #점이 잇으면 큐에 추가, 
    while q:


N = int(input())
tree = [[0]*(N+1) for _ in range(N+1)]

for i in range (N):
    nums = list(map(int,input().split()))
    t = int((len(nums)-2)/2) #len이 8이면 t=3, > 0,1,2
    for k in range (t):
        tree[nums[0]][nums[2*k+1]] = nums[2*k+2]

#각 점에서 bfs 한번씩 수행.
bfsres = []

for points in range (1,N+1):
    visited = [[0]*N+1]
    bfsres.append(bfs(points))

print(max(bfsres))