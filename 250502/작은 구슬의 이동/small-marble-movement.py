n, t = map(int, input().split())

r, c, d = input().split() # d 는 U, D, R, L
r, c = int(r)-1, int(c)-1 # 초기 R행 C열

mapper = {
    "R" : 0,
    "D" : 1,
    "U" : 2,
    "L" : 3
}

move_dir = mapper[d]

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = r + dxs[move_dir], c + dys[move_dir]
    if in_range(nx, ny):
        r, c = nx, ny
        # r += dxs[move_dir]
        # c += dys[move_dir]

    else:
        move_dir = 3 - move_dir
print(r+ 1, c+ 1)


