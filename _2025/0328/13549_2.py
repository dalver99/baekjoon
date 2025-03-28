from collections import deque

N, K = map(int, input().split())
tries = deque([(K, 0)])
visited = set()  # To track visited numbers

while tries:
    now, now_time = tries.popleft()
    
    # If we reach N, return the number of steps
    if now == N:
        print(now_time)
        break

    # Avoid revisiting the same number
    if now in visited:
        continue
    visited.add(now)

    # Explore possible moves
    if now % 2 == 0 and now > N:
        tries.append((now // 2, now_time + 1))
    else:
        tries.append((now + 1, now_time + 1))
        tries.append((now - 1, now_time + 1))
