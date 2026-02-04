n, m = tuple(map(int, input().split())) # nxn, 연속해야하는 숫자 최소 m
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def check_validate(j, m):
    return j+m <= n

# 행으로 봐서 연속하는지 계산
for i in range(n):
    for j in range(n):
        if check_validate(j, m):
            row_temp_list= []
            for k in range(m):        
                row_temp_list.append(grid[i][j+k])        
            if len(set(row_temp_list)) == 1:
                answer += 1
                break

# 열로 봐서 연속하는지 계산 (grid를 y=x 대칭)
transformed_grid = [[0]*n for _ in range(n)]

for p in range(n):
    for q in range(n):
        transformed_grid[p][q] = grid[q][p]

for i in range(n):
    for j in range(n):
        if check_validate(j, m):
            col_temp_list= []
            for k in range(m):        
                col_temp_list.append(transformed_grid[i][j+k])        
            if len(set(col_temp_list)) == 1:
                answer += 1
                break

print(answer)
