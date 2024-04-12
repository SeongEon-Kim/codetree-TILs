n = int(input())
_list = [list(input().split()) for _ in range(n)]

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for idx in range(n):
    if _list[idx][0] == "E":
        for j in range(int(_list[idx][1])):
            x, y = x + dx[0], y + dy[0]
    elif _list[idx][0] == "S":
        for j in range(int(_list[idx][1])):
            x, y = x + dx[1], y + dy[1]
    elif _list[idx][0] == "W":
        for j in range(int(_list[idx][1])):
            x, y = x + dx[2], y + dy[2]
    elif _list[idx][0] == "N":
        for j in range(int(_list[idx][1])):
            x, y = x + dx[3], y + dy[3]
    
print(x, y, sep=" ")