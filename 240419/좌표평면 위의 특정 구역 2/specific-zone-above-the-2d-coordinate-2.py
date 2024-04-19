import sys

n = int(input())
_list = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    min_area = sys.maxsize
    max_height = 0
    max_width = 0
    min_height = sys.maxsize
    min_width = sys.maxsize
    for j in range(n):
        if i == j:
            continue
        if _list[j][0] >= max_height:
            max_height = _list[j][0]
        if _list[j][0] <= min_height:
            min_height = _list[j][0]
        if _list[j][1] >= max_width:
            max_width = _list[j][1]
        if _list[j][1] <= min_width:
            min_width = _list[j][1]
    area = (max_height - min_height) * (max_width - min_width)
    min_area = min(min_area, area)
print(min_area)