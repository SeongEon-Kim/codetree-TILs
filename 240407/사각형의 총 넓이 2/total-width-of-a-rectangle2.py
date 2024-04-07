n = int(input())

offset = 100
max_r = 200

rectangle_list = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for i in range(x1, x2):
        for j in range(y1, y2):
            rectangle_list[i][j] = 1

cnt =0
for i in range(max_r+1):
    for j in range(max_r+1):
        if rectangle_list[i][j]:
            cnt+=1

print(cnt)