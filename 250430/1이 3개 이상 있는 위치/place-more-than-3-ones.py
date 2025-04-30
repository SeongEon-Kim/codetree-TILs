n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0,-1,0,1]

answer = 0
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def adjacent_cnt(x, y):
    near_cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] ==1:
            near_cnt +=1
    return near_cnt

for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            answer += 1
    
print(answer)
