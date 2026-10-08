# 코딩테스트 특강 (10.08)
# 이론 
# <기본형> 
'''
def dfs(cur):
    visited[cur] = True
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)
'''
# <격자 DFS>
'''
def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 격자, DFS, 뱀 조건
        if not in_range(nx, ny) or visited[nx][ny] or grid[nx][ny] ==0:
            continue
        
        dfs(nx, ny)
'''

# 문제 풀이
n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
x, y = 0, 0
dx, dy = [0, 1], [1, 0]

def in_range(x, y):
    return 0<= x < n and 0<= y < m

def dfs(x, y):
    visited[x][y] = True # 방문처리
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny) or graph[nx][ny] == 0 or visited[nx][ny]: # 방문 대상 x
            continue
        
        dfs(nx, ny) # 다음 노드 방문

dfs(0,0)          
if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)

# ---

# 그래프 탐색의 특성
# 정점과 연결된 그래프 전체를 탐색할 수 있다. (-> 좌측 상단 출발에서 특정 지점 도달 가능성 탐색)
# 아, 격자를 그래프 형태로 변환해야겠다!
# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]

# dxs, dys = [0, 1], [1, 0]
# escape_status = False

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# def dfs(x, y):
#     global escape_status
#     if escape_status:
#         return

#     for dx, dy in zip(dxs, dys):
#         nx, ny = x + dx, y + dy
#         if in_range(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
#             visited[nx][ny] = True
#             if nx == n - 1 and ny == m - 1:
#                 escape_status = True
#                 return
#             dfs(nx, ny)

# # 시작이 막혔으면 실패
# if grid[0][0] == 0:
#     print(0)
# # 시작이 곧 도착(1x1)이면 시작칸이 1일 때 성공
# elif n == 1 and m == 1:
#     print(1)
# else:
#     visited[0][0] = True
#     dfs(0, 0)
#     print(1 if escape_status else 0)


'''
# DFS 방법 1
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 주어진 격자를 벗어나는지 여부를 반환
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 주어진 위치로 이동할 수 있는지 여부를 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)
        
visited[0][0] = 1
dfs(0,0)

print(visited[n-1][m-1])
'''