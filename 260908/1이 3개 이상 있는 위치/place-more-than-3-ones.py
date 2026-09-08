# 격자의 상하좌우(4칸)칸 중 1이 적혀있는 칸의 수가 3개 이상이면 +1

ans = 0

n = int(input())
arr_list = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return (x >= 0 and x < n) and (y >= 0 and y < n)

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if in_range(x, y) and arr_list[x][y] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)