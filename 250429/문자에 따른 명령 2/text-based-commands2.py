dirs = input()

# Please write your code here.
# L -> 왼 90도 회전
# R -> 오 90도 회전
# F -> 앞으로 전진
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0,-1,0,1]
direct = 3

for c_dir in dirs:
    # 반시계방향 90' 회전
    if c_dir == 'L':
        direct = (direct - 1 + 4) % 4
    # 시계방향 90' 회전
    elif c_dir == 'R':
        direct = (direct + 1) % 4
    # 직진
    else:
        x, y = x + dx[direct], y + dy[direct]

print(x, y)