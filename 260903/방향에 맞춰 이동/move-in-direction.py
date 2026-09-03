N = int(input())

x, y = 0, 0

for i in range(N):
    dx, dy = tuple(input().split())
    dy = int(dy)
    if dx == "N":
        x += 0
        y += dy
    elif dx == "E":
        x += dy
        y += 0
    elif dx == "S":
        x += 0
        y += -dy
    elif dx == "W":
        x += -dy
        y += 0
print(x, y, end =" ")