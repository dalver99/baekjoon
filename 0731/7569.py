from collections import deque

def bfs():
    directions = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in directions:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                q.append((nz, ny, nx))

M, N, H = map(int, input().split())
box = []
q = deque()

for h in range(H):
    layer = []
    for n in range(N):
        xline = list(map(int, input().split()))
        layer.append(xline)
        for m in range(M):
            if xline[m] == 1:
                q.append((h, n, m))
    box.append(layer)

# Perform BFS starting from all initially ripe tomatoes
bfs()

# Determine the maximum number of days needed
max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:  # Unripe tomato found
                print(-1)
                exit()
            max_days = max(max_days, box[h][n][m])

print(max_days - 1)  # Subtract 1 to get the number of days (since initial ripe tomatoes are marked as 1)