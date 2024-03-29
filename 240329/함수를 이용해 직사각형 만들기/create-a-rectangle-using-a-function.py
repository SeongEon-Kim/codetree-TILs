def print_rect(n, m):
    for _ in range(n):
        print("*" * m)


row_num, col_num = tuple(map(int, input().split()))
print_rect(row_num, col_num)