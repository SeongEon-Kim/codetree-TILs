import sys

n = int(input())
_list = list(map(int, input().split()))

min_distance = sys.maxsize
for idx in range(n):
    distance = 0
    for j in range(n):
        distance += abs(_list[j]*(idx-j))
    min_distance = min(min_distance, distance)
print(min_distance)