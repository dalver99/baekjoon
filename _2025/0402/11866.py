import sys

N, K = map(int,input().split())

circle = []
popped = []
for i in range (N):
    circle.append(i+1)

index = 0
while len(circle) > 0:
    index += K-1
    index %= len(circle)
    popped.append(circle.pop(index))

print('<' + ', '.join(map(str,popped)) + '>')