N = int(input())
x, y = 0, 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

mapper = {
    "N": 3,
    "E": 0,
    "S": 1,
    "W": 2
}

for i in range(N):
    line = input().split()
    dir_c = line[0]
    dist = int(line[1])
    
    dir_num = mapper[dir_c]

    x += dx[dir_num] * dist
    y += dy[dir_num] * dist
    
print(x, y, end =" ")