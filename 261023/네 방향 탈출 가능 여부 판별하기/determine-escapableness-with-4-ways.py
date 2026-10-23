# 코딩테스트 특강 (10.08)
# 이론 
# <기본형> 
# BFS는 방문처리를 미리한다.(배열을 사용하면 방문처리 미리 해줘야하지만 Queue를 사용하면 된다)
# from collections import deque

# que = deque()
# visited = [False for i in range(n)]


# def bfs(start):
#     que.append(start) # 시작 노드 넣기
#     visited[start] = True # 바로 방문처리

#     while len(que) > 0: # 비어있지 않는 동안
#         cur = que[0]
#         que.popleft()

#         for nxt in v[cur]:
#             if visited[nxt]:
#                 continue
#             que.append(nxt)
#             visited[nxt] = True


# <격자 BFS 기본형> 
# from collections import deque

# que = deque()
# visited = [[False for i in range(m)] for i in range(n)]

# def bfs(x, y):
#     que.append([x, y]) # 시작 노드 넣기
#     visited[x][y] = True # 바로 방문처리

#     while len(que) > 0: # 비어있지 않는 동안
#         x = que[0][0]
#         y = que[0][1]
#         que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if not in_range(nx, ny) or visited[nx][ny] or que[nx][ny] == 0:
#                 continue
#             que.append([nx,ny])
#             visited[nx][ny] = True


from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x,y):
    return 0<= x < n and 0<= y < m 

def bfs(x, y):
    que = deque()
    que.append([x, y]) # 시작 노드 넣기
    visited[x][y] = True # 바로 방문처리

    while len(que) > 0: # 비어있지 않는 동안
        x = que[0][0]
        y = que[0][1]
        que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 0:
                continue
            que.append([nx,ny])
            visited[nx][ny] = True

bfs(0,0)

if visited[n-1][m-1] == 1 :
    print(1)
else:
    print(0)


'''        
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
'''