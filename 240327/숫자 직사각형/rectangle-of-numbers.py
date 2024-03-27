n, m = list(map(int, input().split()))
arr_2d = [[0 for _ in range(m)] for _ in range(n)]

start_element_value = 1

for i in range(n):
    for j in range(m):
        arr_2d[i][j] = start_element_value
        start_element_value += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=" ")
    print()