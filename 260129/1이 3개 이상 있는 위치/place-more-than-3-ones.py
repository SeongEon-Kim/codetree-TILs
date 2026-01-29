n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
ans = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(n): # [[0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 0]]
    for j in range(n): # [0, 1, 0, 1]
        cnt = 0 
        for k in range(4): # 동, 남, 서, 북
            dx = i + dxs[k]
            dy = j + dys[k]
            if in_range(dx, dy) and grid[dx][dy] == 1:
                cnt +=1
        if cnt >= 3:
            ans +=1
print(ans)