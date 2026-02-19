# 그래프 탐색의 특성
# 정점과 연결된 그래프 전체를 탐색할 수 있다. (-> 좌측 상단 출발에서 특정 지점 도달 가능성 탐색)
# 아, 격자를 그래프 형태로 변환해야겠다!
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxs, dys = [0, 1], [1, 0]
escape_status = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    global escape_status
    if escape_status:
        return

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            if nx == n - 1 and ny == m - 1:
                escape_status = True
                return
            dfs(nx, ny)

# 시작이 막혔으면 실패
if grid[0][0] == 0:
    print(0)
# 시작이 곧 도착(1x1)이면 시작칸이 1일 때 성공
elif n == 1 and m == 1:
    print(1)
else:
    visited[0][0] = True
    dfs(0, 0)
    print(1 if escape_status else 0)