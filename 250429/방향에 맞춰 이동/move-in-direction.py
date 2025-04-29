n = int(input())

x, y = 0, 0
dx, dy = [1,0,-1, 0], [0, -1, 0, 1]

for _ in range(n):
    direction, step = tuple(map(str,input().split()))
    step = int(step)
    if direction =="E":
        i = 0
        x, y = x + (step * dx[i]), y + (step *dy[i])
    elif direction == "S":
        i = 1
        x, y = x + (step * dx[i]), y + (step *dy[i])
    elif direction =="W":
        i = 2
        x, y = x + (step * dx[i]), y + (step *dy[i])
    else : # direction =="N":
        i = 3
        x, y = x + (step * dx[i]), y + (step *dy[i])

print(x,y, end=" ")