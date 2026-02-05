# # 격자 크기 n, 시작 r, c
# n, r, c = tuple(map(int, input().split()))

# # n x n 주어짐
# grid = [ list(map(int,input().split())) for _ in range(n)]
# print(n, r, c, grid)


# max_value = grid[r][c] # 초기 최댓값
# find_max = 0
# answer_list = []

# def in_range(r, c): # 범위 체크
#     return r < n and c < n

# def move(r, c, max_value):
#     drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 우선 순위
    
#     for dr, dc in zip(drs, dcs):
#         move_r, move_c = r + dr, c + dc # 상 하 좌 우 순으로 이동
        
#         if grid[move_r][move_c] > max_value: # 기존 값(max) 보다 크다면
#             max_value = grid[move_r][move_c] # 최댓값 변경
#             r, c = r + dr, c + dc # 좌표 이동
#             answer_list.append(r, c) # 이동 좌표 입력
#             find_max = 1 # 우선 순위 적용 되면 바로 통과
#             return answer_list # 이동한 위치 반환
#     return r, c # 이동 안하면 현재 위치 반환

# result = []
# for i in range(n):
#     for j in range(n):
#         result.append(move(i, j, max_value))

# print(result)


# # 격자 크기 n, 시작 r, c
# n, r, c = tuple(map(int, input().split()))

# # n x n 주어짐
# grid = [ list(map(int,input().split())) for _ in range(n)]
# print(n, r, c, grid)


# max_value = grid[r][c] # 초기 최댓값
# find_max = 0
# answer_list = []

# def in_range(r, c): # 범위 체크
#     return r < n and c < n

# def move(r, c, max_value):
#     drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 우선 순위
    
#     for dr, dc in zip(drs, dcs):
#         move_r, move_c = r + dr, c + dc # 상 하 좌 우 순으로 이동
        
#         if grid[move_r][move_c] > max_value: # 기존 값(max) 보다 크다면
#             max_value = grid[move_r][move_c] # 최댓값 변경
#             r, c = r + dr, c + dc # 좌표 이동
#             answer_list.append(r, c) # 이동 좌표 입력
#             find_max = 1 # 우선 순위 적용 되면 바로 통과
#             return answer_list # 이동한 위치 반환
#     return r, c # 이동 안하면 현재 위치 반환

# result = []
# for i in range(n):
#     for j in range(n):
#         result.append(move(i, j, max_value))

# print(result)

n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# r, c가 1부터 주어지는 경우(대부분) -> 0-index로 변환
r -= 1
c -= 1

drs = [-1, 1, 0, 0]   # 상, 하, 좌, 우
dcs = [0, 0, -1, 1]

path = [grid[r][c]]   # 시작 칸 포함

while True:
    cur = grid[r][c]
    moved = False

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > cur:
            r, c = nr, nc
            path.append(grid[r][c])
            moved = True
            break

    if not moved:
        break

print(*path)