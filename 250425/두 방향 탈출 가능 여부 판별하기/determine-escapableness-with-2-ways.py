n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*(m+1) for _ in range(n)]
answer = [[0]*(m+1) for _ in range(n)]
# Please write your code here.
print(n,m, grid)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] ==0:
        return False
    return True


def dfs(x,y):
    global order
    dxs, dys = [ 1, 0 ], [0, -1] # 동, 남

    for dx, dy = zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            answer[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

order = 1
answer[0][0] = order
order += 1
visited[]