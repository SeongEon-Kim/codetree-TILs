import sys
from collections import deque

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

a = [list(map(int, input().split())) for _ in range(n)]

# bfs 변수
q = deque()
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한
# 최단 거리 기록
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 격자를 벗어나지 않으면서, 뱀도 없고, 방문한 적 없는 곳이면
# 지금 이동하는 것이 최단 거리를 보장할 수 있다 -> Go
def can_go(x,y):
    return in_range(x, y) and a[x][y] and not visited[x][y]

# queue에 새로운 위치를 추가하고 방문 여부를 표시
# 시작점으로 부터의 최단 거리 값도 갱신
def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = True
    step[new_x][new_y] = new_step

# bfs를 통해 최소 이동 횟수를 구함
def find_min():
    global ans
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # queue에 남은 것이 없을 때 까지 반복
    while q:
        # 가장 먼저 들어온 원소를 뺀다
        x, y = q.popleft()

        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이면
            # 새로운 queue에 넣어준다
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단거리에 1이 증가
                push(new_x, new_y, step[x][y] + 1)
        
    # 우측 하단에 가는 것이 가능할때만 답을 갱신
    if visited[n-1][m-1]:
        ans = step[n-1][m-1]

# bfs를 이용해 최소 이동 횟수를 구함
# 시작점을 queve에 넣고 시작
push(0, 0, 0)
find_min()

# 불가능하면 -1을 답으로 넣어줌
if ans == INT_MAX:
    ans = -1

print(ans)