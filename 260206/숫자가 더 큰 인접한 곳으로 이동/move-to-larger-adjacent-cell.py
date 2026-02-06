n, c, r = tuple(map(int, input().split()))
grid = [ list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
visited_nums = []
max_value = grid[c-1][r-1]
visited_nums.append(max_value) # 초기 최댓값 


def in_range(move_c, move_r):
    return 0 < move_c <= n and 0 < move_r <= n

def simulate(dxs, dys): # 이동 작업
    global c, r, max_value # 2, 2, 5
    for dx, dy in zip(dxs, dys):
        move_c, move_r = c + dx , r + dy # 2, 2 => 3, 2

        if in_range(move_c, move_r): # 범위 내에 있으면
            position_value = grid[move_c-1][move_r-1] # 번째 -> 인덱스
            # print("position_value, move_c, move_r", position_value, move_c, move_r)
            if position_value > max_value: # 최댓값보다 해당 위치가 더 크면
                max_value = position_value # 최댓값 갱신
                c, r = move_c, move_r # 현위치 갱신
                # print("c, r", c, r) # 3, 2
                return True # 이동 완료

        else: # 범위 밖에 있으면
            continue # 이동 불가
    return False # 범위 내 이동 불가 종료

while True:
    move = simulate(dxs, dys) 
    if not move: # 이동불가
        break # while 문 탈출
    visited_nums.append(grid[c-1][r-1])

for i in visited_nums:
    print(i, end= " ")


'''
# 변수 선언 및 입력
n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문하게 되는 숫자들을 담을 곳입니다.
visited_nums = []


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인합니다.
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num


# 조건에 맞춰 움직여봅니다.
# 움직였다면 true를 반환하고
# 만약 움직일 수 있는 곳이 없었다면 false를 반환합니다.
def simulate():
    global curr_x, curr_y
    
    # 코딩의 간결함을 위해 
    # 문제 조건에 맞게 상하좌우 순서로
    # 방향을 정의합니다.
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        # 갈 수 있는 곳이라면
        # 이동하고 true를 반환합니다.
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True
    
    # 움직일 수 있는 곳이 없었다는 의미로
    # false 값을 반환합니다.
    return False


# 초기 위치에 적혀있는 값을 답에 넣어줍니다.
visited_nums.append(a[curr_x][curr_y])
while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = simulate()
    
    # 인접한 곳에 더 큰 숫자가 없다면 종료합니다.
    if not greater_number_exist:
        break
    
    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited_nums.append(a[curr_x][curr_y])

# 출력:
for num in visited_nums:
    print(num, end=' ')

'''