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

# 모범 답안
'''
# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# (row_s, col_s) ~ (row_e, col_e) 사이의 금의 개수를 계산합니다.
def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += grid[row][col]

    return num_of_gold


max_gold = 0

# (row, col)이 3 * 3 격자의 좌측 상단 모서리인 경우를 전부 탐색합니다. 
for row in range(n):
    for col in range(n):
        # 3 * 3 격자가 n * n 격자를 벗어나는 경우는 계산하지 않습니다.
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)
            
        # 최대 금의 개수를 저장합니다.
        max_gold = max(max_gold, num_of_gold)

print(max_gold)
'''