N,K = map(int,input().split())

#2배씩 막 늘어나면 어차피 금방 찾는다. BFS로 하자.
visited = [-1] * 100001

from collections import deque
q = deque()

q.append((N))
visited[N] = 0

while q:
    where = q.popleft()
    print(visited[where], end= ' ')
    if where == K:
        print(visited[where])
        break

    for next in (2*where,where-1,where+1):
        if next == 2*where and next <= 100000 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[where]
        elif 0<= next <= 100000 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[where] +1

#사실 굉장히 생각할 게 많다.
#이 알고리즘으로는 visited가 매번 최소인지 보장되는 지 나는 정확히 모르는 상태로 풀었다.

#큐에 뭔가가, 항상 추가시간이 들지 않는거부터 들어가나?
#이를 확인하기 위한 코드가 추가되어있따. 
#또 꼭 그렇진 않음 ... 