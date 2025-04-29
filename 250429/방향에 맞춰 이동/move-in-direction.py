n = int(input())

x, y = 0, 0

dxs, dys = [1,0,-1,0], [0,-1,0,1]

move = 0

# c_dir_dic = {"E":0, "W":1, "S":2, "N:3"}

for _ in range(n):
    dirs, steps = tuple(map(str, input().split()))
    steps = int(steps)

    if dirs=="E":
        move = 0
    elif dirs=="S":
        move = 1
    elif dirs=="W":
        move=2
    else:
        move=3
    
    x, y = x +(steps*dxs[move]), y + (steps*dys[move])

print(x, y)