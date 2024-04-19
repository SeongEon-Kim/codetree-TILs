import sys

n = int(input())
_list = [tuple(map(int, input().split())) for _ in range(n)]

min_area = []
for i in range(n):
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
        if area != 0:
            min_area.append(area)

print(min(min_area))