from collections import deque

# 입력: N(격자크기), K(시작점 개수)
n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

q = deque()
count = 0

for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    if grid[r][c] == 0 and not visited[r][c]:
        visited[r][c] = True
        q.append((r, c))
        count += 1

while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
            visited[nx][ny] = True
            q.append((nx, ny))
            count += 1

print(count)