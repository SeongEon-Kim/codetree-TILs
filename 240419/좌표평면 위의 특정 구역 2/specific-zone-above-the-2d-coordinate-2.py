import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX

# 빼야하는 점의 위치를 정합니다.
for i in range(n):
    # i번 점을 제외한 나머지 점들을 포함하기 위한
    # 직사각형의 최소 넓이를 구합니다.

    # 직사각형의 최소 넓이를 구하기 위해서는,
    # 남은 점들의 x좌표 중 최소, 최대
    #          y좌표 중 최소 최대를 구해야 합니다.
    min_x, max_x = INT_MAX, 1
    min_y, max_y = INT_MAX, 1
    for j, (x, y) in enumerate(points):
        # i번째 점은 제외합니다.
        if j == i:
            continue

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    # 가능한 직사각형 넓이 중 최솟값을 기록합니다.
    ans = min(ans, (max_x - min_x) * (max_y - min_y))

print(ans)

# import sys

# n = int(input())
# _list = [tuple(map(int, input().split())) for _ in range(n)]

# min_area = []
# for i in range(n):
#     max_height = 0
#     max_width = 0
#     min_height = sys.maxsize
#     min_width = sys.maxsize
#     for j in range(n):
#         if i == j:
#             continue
#         if _list[j][0] >= max_height:
#             max_height = _list[j][0]
#         if _list[j][0] <= min_height:
#             min_height = _list[j][0]
#         if _list[j][1] >= max_width:
#             max_width = _list[j][1]
#         if _list[j][1] <= min_width:
#             min_width = _list[j][1]
#         area = (max_height - min_height) * (max_width - min_width)
#         print(area)
#         if area != 0:
#             min_area.append(area)

# print(min(min_area))