import sys
input = sys.stdin.readline

N = int(input())
ishere = set(list(map(int,input().split())))

M = int(input())
inthere = list(map(int,input().split()))

for i in range (M):
    result = inthere[i] in ishere
    print (1 if result else 0)