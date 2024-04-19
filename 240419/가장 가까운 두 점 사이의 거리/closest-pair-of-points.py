import sys

n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]

min_distance = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        distance = (_list[i][0] - _list[j][0])**2 + (_list[i][1] - _list[j][1])**2
    min_distance = min(min_distance, distance)
print(min_distance)