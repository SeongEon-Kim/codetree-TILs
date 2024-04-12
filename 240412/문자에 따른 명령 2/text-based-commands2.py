str = list(str(input()))

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_name = 3 

for idx in range(len(str)):
    if str[idx] == "L":
        dir_name = (dir_name -1 + 4) % 4

    elif str[idx] == "R":
        dir_name = (dir_name + 1) % 4
    
    elif str[idx] == "F":
        x , y = x + dx[dir_name], y + dy[dir_name]

print(x, y, sep=" ")