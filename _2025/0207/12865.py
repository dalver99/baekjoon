N,K = map(int,input().split())
moolgun = []
for _ in range (N):
    w,v = map(int,input().split())
    moolgun.append([w,v])

dp = [[0]*N+1 for _ in range (N+1)]