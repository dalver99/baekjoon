import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [list(input().strip()) for _ in range (R)]

maxlen = 1

def dfs (point,listt):
    global maxlen
    maxlen = max(maxlen,len(listt))
    if maxlen ==26:
        return
    x,y = point
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    for points in moves:
        nx = x+points[0]
        ny = y+points[1]
        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in listt:
            char = board[ny][nx]
            listt.add(char)
            dfs((nx,ny),listt)
            listt.remove(char)

dfs((0,0),{board[0][0]})
print(maxlen)

