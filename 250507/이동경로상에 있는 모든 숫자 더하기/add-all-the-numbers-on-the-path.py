N, T = map(int, input().split())
input_str = input()
board = [list(map(int, input().split())) for _ in range(N)]

x = N // 2 
y = N // 2 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 3
answer = 0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

answer += board[x][y]
for i in input_str:
    if i =="R":
        direction = (direction + 1)%4
    elif i =="L":
        direction = (direction + 3)%4
    else: # F
        new_x = x + dxs[direction]
        new_y = y + dys[direction]
        if in_range(new_x, new_y):
            x = x + dxs[direction]
            y = y + dys[direction]
            answer += board[x][y]

print(answer)