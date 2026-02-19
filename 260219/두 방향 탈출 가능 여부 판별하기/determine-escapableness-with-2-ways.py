# 그래프 탐색의 특성
# 정점과 연결된 그래프 전체를 탐색할 수 있다. (-> 좌측 상단 출발에서 특정 지점 도달 가능성 탐색)
# 아, 격자를 그래프 형태로 변환해야겠다!
n, m = tuple(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxs, dys = [0, 1], [1, 0]
x, y = 0, 0
escape_status = False

def in_range(x, y):
    return 0<= x < n and 0<= y < m # x, y는 index(0, 0)

def dfs(x, y):
    global escape_status
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and grid[nx][ny] != 0 and visited[nx][ny] == False: 
            # 범위 내 & 뱀 x & 방문 x
            visited[nx][ny] = True # 방문
            if nx == n-1 and ny == n-1:
                escape_status = True
            dfs(nx, ny)
    
visited[x][y] = True # 방문
dfs(x, y) 

if escape_status:
    print(1)
else:
    print(0)