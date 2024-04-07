n = int(input())

lines = [list(map(int,input().split())) for _ in range(n)]

overlap_num = 0
min_value = 0

for idx in range(n):
    if min_value > lines[idx][0]:
        min_value = lines[idx][0]

if min_value < 0:
    for idx in range(n):
        lines[idx][0] -= min_value
        lines[idx][1] -= min_value

overlap_list = [0 for _ in range(201)] # 0 ~ 201

for j in range(n):
    for k in range(lines[j][0], lines[j][1]):
        overlap_list[k] += 1

print(max(overlap_list))