import sys
input = sys.stdin.readline

N = int(input())

coords = []
for _ in range (N):
    x,y = map(int,input().split())
    coords.append([x,y])
sort_coords = sorted(coords,key=lambda x: (x[0],x[1]))

for dots in sort_coords:
    print(*dots)