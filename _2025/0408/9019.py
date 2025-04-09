import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    n = n*2%10000
    return n

def S(n):
    n = (n-1)%10000
    return n
    
def L(n):
    l = (n//1000)+(n%1000)*10
    return l
    
def R(n):
    r = (n//10)+(n%10)*1000
    return r
##

T = int(input())
for _ in range(T):
    q = deque()
    fromthis,tothis = map(int,input().split())
    q.append([fromthis,""])
    visited = [False]*10001
    while q:
        where,command = q.popleft()
        #print(where,command)

        if where == tothis:
            print(command)
            break

        d = D(where)
        if visited[d] == False:
            visited[d] = True
            q.append([d,command+"D"])

        s = S(where)
        if visited[s] == False:
            visited[s] = True
            q.append([s,command+"S"])

        l = L(where)
        if visited[l] == False:
            visited[l] = True
            q.append([l,command+"L"])

        r = R(where)
        if visited[r] == False:
            visited[r] = True
            q.append([r,command+"R"])