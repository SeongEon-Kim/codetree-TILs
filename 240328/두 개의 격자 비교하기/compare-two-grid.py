n, m = list(map(int, input().split()))

first_arr = [list(map(int, input().split())) for _ in range(n)]
second_arr = [list(map(int, input().split())) for _ in range(n)]

result_arr = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        if first_arr[i][j] == second_arr[i][j]:
            result_arr[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result_arr[n][m], end= " ")
    print()