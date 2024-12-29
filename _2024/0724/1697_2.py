from collections import deque

n, k = map(int, input().split())
max_size = 10**5
dist = [-1] * (max_size+1)
dist[n] = 0
queue = deque([n])

while queue:
    v = queue.popleft()
    for next_step in [v-1, v+1, v*2]:
        if 0 <= next_step <= max_size and dist[next_step] == -1:
            dist[next_step] = dist[v] + 1
            queue.append(next_step)

print(dist[k])