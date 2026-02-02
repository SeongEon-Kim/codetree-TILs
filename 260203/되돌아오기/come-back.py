n = int(input())
moves = [tuple(input().split()) for _ in range(n)] # N 3
# grid = [[0]*10 for _ in range(10)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # E, S, W, N
dir = 0
x, y = 0, 0
time = 0

dir_map = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

found = 0

for d, k in moves: # 방향, 거리 ex) N 3
    for _ in range(int(k)): # ex) 3
        dir = dir_map[d] # ex) N => 3
        x, y = x + dxs[dir], y + dys[dir]
        time += 1 
        #print(x, y)
        if x == 0 and y == 0:
            print(time)
            found = 1
            break
    if found:
        break
if not found:
    print(-1)