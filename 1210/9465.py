import sys
input = sys.stdin.readline()

T = int(input())
for _ in range (T):
    N = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]

    #2행 DP배열 형성