import sys

N, M = map(int,sys.stdin.readline().rstrip().split())

layer = []
for _ in range (N):
    xline = list(map(int, input().split()))
    layer.append(xline)
print(layer)

attempt = [[0]*M for _ in range (N)]
print(attempt)

tested = []



if N+M <= 3:
    print('0')
else:
    ##Algorithm