#지금까지 지난칸과 모두 달라야하니까, DP처럼 중복문제로 풀 수는 없을. .... .. .. 듯?
#BFS보다는 DFS가 좀 생각하기 편할듯.. 최대길이 정해놓고 안됐으면 그냥 탈락 됐으면 갱신

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
#근데 visited를 어떻게 .. 관리하지? 모르겠네 안해볼까
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    for points in moves:
        dx,dy = points
        nx = x+dx
        ny = y+dy
        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in listt:
            char = board[ny][nx]
            listt.add(char)
            dfs((nx,ny),listt)
            listt.remove(char)

dfs((0,0),{board[0][0]})
print(maxlen)

