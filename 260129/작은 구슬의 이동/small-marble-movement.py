n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

grid = [[0] * n for _ in range(n)]
#dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
dxs = [0, 1, -1,  0]
dys = [1, 0,  0, -1]
wordtodir = {
    "R": 0,
    "D": 1,
    "L": 2,
    "U": 3
}
direction = wordtodir[d]

def in_range(x, y):
    return 1 <= x and x < n and 1 <= y and y < n

def move(a, b, d): # direction, t 만큼 반복
    if in_range(a + dxs[d], b + dys[d]): # 다음 이동이 격자 안에 있으면, 방향으로 한 칸씩 이동
        a = a + dxs[d]
        b = b + dys[d]
    else: # 격자 안에 없으면 방향만 변경
        # 0 <-> 2, 1 <-> 3 / d = (d + 2) % 4
        d = (d + 2) % 4

    return a, b, d

for i in range(t): # t초 동안
    r, c, direction = move(r, c, direction)
print(r, c)
