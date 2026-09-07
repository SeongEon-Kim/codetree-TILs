'''
1. [앞선 문제 상황]
x, y 좌표 관리
dir_num 입력

2. 바라보고 있는 방향이 있는 사람
x, y, "dir_num" 관리
명령: 직진, 우회전, 좌회전 등
'''


x, y = 0, 0
dir_num = 3 # 0, 1, 2, 3 (반시계)
dx = [1, 0, -1 ,0]
dy = [0, -1, 0, 1]

# L: 왼쪽 90 => -1
# R: 오른쪽 90 => +1
# F: dir_num에 따라 다름 

command_list = list(map(str, input()))

for i in command_list:
    if i == "L":
        dir_num = (dir_num - 1 + 4)%4
    elif i == "R":
        dir_num = (dir_num + 1)%4
    else: # F:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)

