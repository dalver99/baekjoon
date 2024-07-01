k,n = map(int,input().split())
cables = [int(input()) for _ in range(k)]
start, end = 1, max(cables)

#binary search가 필요하다
while start <= end:
    mid = (start + end) // 2   
    lines = [cable // mid for cable in cables]
    if sum(lines) >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)