# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(2)]
u_grid = grid[0]
d_grid = grid[1]

for _ in range(t):
    pass
    # Step 1
    # 위에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장해놓습니다.
    temp = u_grid[-1]

    # Step 2
    # 위에 있는 숫자들을 완성합니다.
    # 오른쪽에서부터 채워넣어야 하며, #맨 왼쪽 숫자는 아래에서 가져와야함에 유의합니다.
    for i in range(n-1, 0, -1):
        u_grid[i] = u_grid[i-1]
    u_grid[0] = d_grid[-1]

    # Step 3
    # 아래에 있는 숫자들을 완성합니다.
    # 마찬가지로 오른쪽에서부터 채워넣어야 하며, #맨 왼쪽 숫자는 위에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
    for j in range(n-1, 0, -1):
        d_grid[j] = d_grid[j-1]
    d_grid[0] = temp

for k in u_grid:
    print(k, end=" ")
print()
for l in d_grid:
    print(l, end=" ")