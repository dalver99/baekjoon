N,K = map(int,input().split())

#2배씩 막 늘어나면 어차피 금방 찾는다. BFS로 하자.
visited = [0] * 100001

from collections import deque
q = deque()

q.append((N,0))
visited[N] = 1

while q:
    where,howmany = q.popleft()
    if where == K:
        print(howmany)
        break

    if where*2 <= 100000 and not visited[where*2]:
        visited[where*2] = 1
        q.append((where*2,howmany)) #비용이 증가하지 않은 경우는 큐에서 우선순위에 둘래요
    else:
        if where + 1 <= 100000 and not visited[where+1]:
            visited[where+1] = 1
            q.append((where+1,howmany+1))
        if where - 1 >= 0 and not visited[where-1]:
            visited[where-1] = 1
            q.append((where-1,howmany+1))