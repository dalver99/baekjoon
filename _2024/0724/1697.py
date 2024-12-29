S,D = map(int,input().split())

visited = [0] * 200001
visited[S] = 1
n = 0
tree = [[] for _ in range(200000)]

if S*2 <= 200000:
    tree[0].append(S*2)
    visited[S*2] = 1
if S-1 >=0:
    tree[0].append(S-1)
    visited[S-1] = 1
if S+1 <= 200000:
    tree[0].append(S+1)
    visited[S+1] = 1

while visited[D] == 0:
    q = tree[n]
    #print(q)
    while len(q)>0:
        now = q.pop(0)
        if now*2<=200000 and now*2 <= D*2+1 and visited[now*2] == 0:
            visited[now*2] = 1
            tree[n+1].append(now*2)
        if now-1>=0 and now-1 >= S/2-1 and visited[now-1] == 0:
            visited[now-1] = 1
            tree[n+1].append(now-1)
        if now+1<=200000 and now+1 >= S/2-1 and visited[now+1] == 0:
            visited[now+1] = 1
            tree[n+1].append(now+1)
    n+=1

if S == D:
    print(n)
else:
    print(n+1)