#파이프의 현재 상태와 끝점만 기억하자.
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
house = []

for _ in range (N):
    house.append(list(map(int,input().split())))

#0 = 가로, 1 = 대각, 2 = 세로 인걸로 하자고.
pipe = (0,(1,0)) #초기상태는 무조건 이거임

#(0,(오른쪽 벽)) -> 종료
#(2,(아래쪽 벽)) -> 종료

#이 네가지가 아니면 진행해서 끝낼 수 있다~!

q = deque()
q.append(pipe)
success = 0
while q:
    curr_status,(curr_coordx,curr_coordy) = q.popleft()
    #print(curr_status,curr_coordx,curr_coordy)
    if curr_coordx == N-1 and curr_coordy == N-1:
        success += 1 
    # elif curr_status == 0 and curr_coordx == N-1:
    #     continue
    # elif curr_status == 2 and curr_coordy == N-1:
    #     continue
    else:
        #가로
        if curr_status != 2 and curr_coordx+1 < N and house[curr_coordy][curr_coordx+1] != 1:
            q.append((0,(curr_coordx+1,curr_coordy)))
        #대각
        if  curr_coordx+1 < N and curr_coordy+1 < N and house[curr_coordy+1][curr_coordx+1] != 1 and house[curr_coordy][curr_coordx+1] != 1 and house[curr_coordy+1][curr_coordx] != 1:
            q.append((1,(curr_coordx+1,curr_coordy+1)))
        #세로
        if curr_status != 0 and curr_coordy+1 < N and house[curr_coordy+1][curr_coordx] != 1:
            q.append((2,(curr_coordx,curr_coordy+1)))

print(success)

#놀랍게도 이는 시간초과가 난다....... 
#특정 점에 방문한 경우를 윷놀이마냥 업어줘야한다.......
#그렇게 안하는 방법은 없나....
