import sys
input = sys.stdin.readline
T = int(input())

for _ in range (T):
    N = int(input())
    stickers = []
    stickers.append(list(map(int,input().split())))
    stickers.append(list(map(int,input().split())))

    print(stickers)