n = 4
arr_2d = []

for _ in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for idx in range(n):
    print(sum(arr_2d[idx]))