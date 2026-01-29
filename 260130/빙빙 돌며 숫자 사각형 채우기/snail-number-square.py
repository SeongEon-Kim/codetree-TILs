n, m = tuple(map(int, input().split()))
answer = [ [0] * m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # R, D, L, U
x, y = 0, 0
dir = 0

location = 1
answer[x][y] = location

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def vacant_number(x, y):
    return answer[x][y] == 0 # 0이 아니면 이미 간 곳(방향 전환)


for i in range(n*m -1): # n x m -1 번 반복
    nx, ny = x + dxs[dir], y + dys[dir]

    if not in_range(nx, ny) or not vacant_number(nx, ny):
        dir = ( dir + 1 )%4
    x, y = x + dxs[dir], y + dys[dir]
    location += 1
    answer[x][y] = location

for k in range(n):
    for l in range(m):
        print(answer[k][l], end = " ")
    print()