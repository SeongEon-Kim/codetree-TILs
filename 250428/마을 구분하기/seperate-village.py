n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [ [0]*n for _ in range(n)]

# 현재 마을의 집 개수를 세기 위한 변수
cnt = 0

# 좌표가 범위 안에 들어가는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동할 수 있는지 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

# DFS를 통해 연결된 집을 모두 방문
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)

villages = [] # 각 마을의 집 개수 저장

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            villages.append(cnt)

villages.sort()

print(len(villages)) # 총 마을 수
for v in villages:
    print(v)          # 각 마을 집 개수 (오름차순)
