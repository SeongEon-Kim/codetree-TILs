n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(n, grid)

max_coin = 0

def get_coin(i, j):
    current_coin = 0
    row_s = i
    row_e = i+2
    col_s = j
    col_e = j+2

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            #print("row, col", row, col)
            if grid[row][col] == 1:
                current_coin += 1 
                #print("current_coin at row, col", current_coin, row, col)
    return current_coin

for i in range(n-2): # n-2 까지 세로
    for j in range(n-2): # n-2 까지 가로
        coin = get_coin(i, j) # 기준점 0,0 에서 부터 3x3 크기 내의 동전 크기를 얻는다.
        if coin > max_coin:
            max_coin = coin

print(max_coin)
