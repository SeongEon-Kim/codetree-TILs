dirs = input()

x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

move = 3
for d in dirs:
    if d == "L":
        # 0 -> 3 -> 2 -> 1 -> 0
        move = (move - 1 + 4) % 4
    elif d == "R":
        # 0 -> 1 -> 2 -> 3 -> 0 
        move = (move + 1) % 4
    elif d == "F":
        x += dx[move]
        y += dy[move]

print(x, y)