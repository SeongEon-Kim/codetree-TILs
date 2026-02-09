from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def get_area(k):
    return k*k + (k+1)*(k+1)

max_gold = 0
max_k = 2 * (n - 1)  # 격자 밖까지 마름모 확장 가능하므로 이 정도면 충분

for sr in range(n):
    for sc in range(n):
        # 중심(sr, sc) 기준으로 k를 늘려가며 확장
        visited = [[False]*n for _ in range(n)]
        q = deque()

        visited[sr][sc] = True
        q.append((sr, sc))

        gold = grid[sr][sc]   # k=0 (자기 자신만)
        if gold * m >= get_area(0):
            max_gold = max(max_gold, gold)

        # k=1부터 max_k까지 "한 겹씩" 확장
        for k in range(1, max_k + 1):
            # 현재 큐에는 거리 (k-1)에 있는 점들이 들어있음
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in zip(drs, dcs):
                    nr, nc = r + dr, c + dc
                    if in_range(nr, nc) and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        gold += grid[nr][nc]  # 새로 포함된 칸의 금 누적

            # k 마름모(맨해튼 거리 <= k) 내 금 개수 = gold
            if gold * m >= get_area(k):
                max_gold = max(max_gold, gold)

print(max_gold)

'''
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 주어진 k에 대하여 마름모의 넓이를 반환합니다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)


# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    return sum([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])


max_gold = 0

# 격자의 각 위치가 마름모의 중앙일 때 채굴 가능한 금의 개수를 구합니다.
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)
            
            # 손해를 보지 않으면서 채굴할 수 있는 최대 금의 개수를 저장합니다.
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)
'''