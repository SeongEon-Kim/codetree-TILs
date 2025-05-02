n, m = map(int, input().split())

str_list = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F",
            7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L",
            13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R",
            19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X",
            25:"Y", 26:"Z"}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
answer = [[0]*m for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 동 남 서 북

answer[x][y] = 1
dir_name = 0

for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_name], y + dys[dir_name]
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_name = (dir_name + 1) % 4
    x, y = x + dxs[dir_name], y + dys[dir_name]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        val = answer[i][j] % 26
        if val == 0:
            val = 26  # 0이면 Z로 매핑
        print(str_list[val], end=" ")
    print()
