#밑으로 내려가는 게 아니라, 밑에서 위를 보고 결정하는 것임. 나 어느쪽에 붙을래
#붙으면서 미리 어디로 갈지 다 정할 수 있음.
import sys
input = sys.stdin.readline
N = int(input())

now = list(map(int,input().split()))
for k in range (N-1):
    next = list(map(int,input().split()))
    new = next
    # if k == 0:
    #     new[0] = next[0] + now[0]
    #     new[1] = next[1] + now[0]
    # else: 
    for i in range(len(next)):
        if i == 0:
            new[i] = next[0] + now[0]
        elif i == (len(next) - 1):
            new[i] = next[i] + now[i-1]
        else:
            new[i] = next[i] + max(now[i],now[i-1])
    now = new

print(max(now))