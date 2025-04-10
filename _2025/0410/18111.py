#왠지 이분탐색을 하고 싶다 
import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())

land = []
# maxx = 0
maxx2 = 0
minn = 0
allsum = 0
anstime = 999999999999
ans = 256
for _ in range (N):
    row = list(map(int,input().split()))
    land.append(row)
    allsum += sum(row)
    # if min(row) < minn:
    #     minn = min(row)
    if max(row) > maxx2:
        maxx2 = max(row)

#print(land) ###

#불가능한거부터 제거. 캔 블록은 다시 쓸 수 있으니까, 전체평균보다 크면 못만듬.
maxx = (allsum+B) // (N*M)
maxx = min(maxx,maxx2)
#print(maxx)

for target in range(minn,maxx+1): #같은 경우 가장 높은 땅으로 업데이트를 위해서 이순으로
    blockreq = 0
    timereq = 0

    for i in range (N):
        for j in range (M):
            now = land[i][j]
            if now > target:
                timereq += 2 * (now-target)
            else:
                timereq += 1 * (target-now)

    if timereq <= anstime:
        ans = target
        anstime = timereq

print(anstime, ans)

##passed only with pypy3