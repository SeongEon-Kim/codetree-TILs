N = int(input())

x, y = 0, 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    dir, len = tuple(input().split())
    len = int(len)
    if dir == "N":
        move = 3        
    elif dir == "E":
        move = 0
    elif dir == "S":
        move = 2
    elif dir == "W":
        move = 1

    x = x + dx[move] * len
    y = y + dy[move] * len
print(x, y)

# 딕셔너리 활용 가능
# c_dir = {"N": 3, "E": 0, "S": 2, "W": 1}