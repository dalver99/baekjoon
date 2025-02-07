import sys
input = sys.stdin.readline

N = int(input())
max_score = [0 for _ in range(N+1)]
stairs = [0]
for _ in range (N):
    stairs.append(int(input()))

max_score[1] = stairs[1]
if N>1:
    max_score[2] = stairs[1] + stairs[2]

for n in range(3,N+1):
    max_score[n] = max(max_score[n-2] + stairs[n], stairs[n-1]+max_score[n-3]+stairs[n])

print(max_score[N])