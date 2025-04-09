import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
sadari = []
for _ in range (N):
    x,y = map(int,input().split())
    sadari.append((x,y))
bam = []
for _ in range (M):
    x,y = map(int,input().split())
    bam.append((x,y))

visited = [False] * 106 #0번칸은 안써

#이미 누가 방문했다는 건, 그 칸에 다 효율적으로 가는 방법이 있다는 뜻임.
def bfs(v):
    #어떤칸에 가고, 간 곳이 사다리나 뱀이면 하자.
    #visited는 둘다 바꾸자. 사다리로 가서 더 빨리 가도 간거다.
    q = deque()
    q.append([v,0]) #지점, 주사위 굴린 횟수루다가.
    visited[v] = True

    while q:
        current,diceno = q.popleft()
        moves = [1,2,3,4,5,6]
        diceno += 1
        for move in moves:
            newp = current+ move
            if visited[newp] == False and newp < 100:
                visited[newp] = True
                flag = False
                for pointfrom, pointto in sadari:
                    if pointfrom == newp:
                        visited[pointto] = True
                        q.append([pointto,diceno])
                        flag = True
                for pointfrom, pointto in bam:
                    if pointfrom == newp:
                        visited[pointto] = True
                        q.append([pointto,diceno])
                        flag = True
                
                if not flag:
                    q.append([newp,diceno])

            elif newp == 100:
                print(diceno)
                sys.exit()

bfs(1)