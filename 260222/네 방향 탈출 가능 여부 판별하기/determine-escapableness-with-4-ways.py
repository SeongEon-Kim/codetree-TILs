from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 4방향 (상, 하, 좌, 우)
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    # 시작/도착이 막혀있으면 바로 불가
    if grid[0][0] == 0 or grid[n-1][m-1] == 0:
        return 0

    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))

    return 0

print(bfs())