import sys

input = sys.stdin.readline

N,M,X = map(int,input().split())

map = [([0] * (N+1))for _ in range (N+1)]
print(map)
# for 