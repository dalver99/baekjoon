import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
#A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
#이 조건으로 인해 그리디로 풀 수 있음. 위의 금액을 채워넣음으로 인해서 아래금액을 넣을 수 없는 경우가 발생하지 않음
coins = deque()

for _ in range(N):
    coins.append(int(input()))

reversed_coins = coins.reverse() #popleft를 하려면 큰거부터 꺼내야함

total = 0

while K != 0:
    now = coins.popleft()
    if now <= K:
        howmany = K//now
        total += howmany
        K -= howmany * now

print(total)