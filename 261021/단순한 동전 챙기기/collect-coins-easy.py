# 숫자가 있으면 동전이 있고, 숫자는 동전의 번호, 해당 위치에 도달해야 얻을 수 있다.
# 시작점에서 적절히 이동해서 최소 3개의 동전을 수집하여 도착점으로 도달하려고 한다.
# 수집은 반드시 숫자 증가하는 순 수집할 수 있고, 같은 위치 2번 지나가도 되고 도착해서 수집 안해도 된다.


# 못 품 ㅠㅠ
###################################################################################################

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

coins = []
start = None
end = None

# 1. 시작점, 도착점, 동전 위치 저장
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
        elif grid[i][j].isdigit():
            coins.append((int(grid[i][j]), i, j))

# 동전 번호 기준 오름차순 정렬
coins.sort()

n = len(coins)
m = 3

answer = []
min_dist = float('inf')


# 2. 두 좌표 사이의 최단 거리
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# 3. 선택한 동전 3개의 총 이동 거리 계산
def calculate():
    global min_dist

    selected = []

    for i in range(n):
        if answer[i] == 1:
            selected.append((coins[i][1], coins[i][2]))

    # 시작점 -> 동전 3개 -> 도착점
    path = [start] + selected + [end]

    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])

    min_dist = min(min_dist, total)


# 4. DFS: N개 중 3개 선택
def choose(curr_num, cnt):
    # 모든 동전을 확인했을 때
    if curr_num == n:
        if cnt == m:
            calculate()
        return

    # 현재 동전을 선택하지 않는 경우
    answer.append(0)
    choose(curr_num + 1, cnt)
    answer.pop()

    # 현재 동전을 선택하는 경우
    answer.append(1)
    choose(curr_num + 1, cnt + 1)
    answer.pop()


# 5. 탐색 실행
choose(0, 0)

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)
