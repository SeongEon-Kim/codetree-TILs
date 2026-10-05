n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0
value = 1
x, y = 0, 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(n):
    for j in range(m):
        arr[x][y] = value 
        
        nx = x + dx[dir]
        ny = y + dy[dir]

        if in_range(nx, ny) and arr[nx][ny] == 0: # 범위에 맞으면 다음 
            x = nx
            y = ny

        else: # 그렇지 않으면 +1  3-> 0
            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
        
        value += 1 

for k in range(n):
    for l in range(m):
        print(arr[k][l], end=" ")
    print()
    

