n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INF = 10000000000
dp = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n - 1, -1, -1):  
        if i == 0 and j == n - 1:  
            dp[i][j] = grid[i][j]
        else:
            best = INF
            if i > 0:      # 위에서 내려오는 경우
                best = min(best, dp[i - 1][j])
            if j < n - 1:  # 오른쪽에서 오는 경우
                best = min(best, dp[i][j + 1])
            dp[i][j] = grid[i][j] + best

print(dp[n - 1][0]) 
'''
# 변수 선언 및 입력:
n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
] 
dp = [
    [0] * n
    for _ in range(n)
]


def initialize():
    # 시작점의 경우 dp[0][n - 1] = num[0][n - 1]으로 초기값을 설정해줍니다
    dp[0][n - 1] = num[0][n - 1]

    # 최우측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + num[i][n - 1]

    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(n - 2, -1, -1):
        dp[0][j] = dp[0][j + 1] + num[0][j]

   
# 초기값 설정
initialize()

# 탐색하는 위치의 위에 값과 우측 값 중에 작은 값에
# 해당 위치의 숫자를 더해줍니다.
for i in range(1, n):
    for j in range(n - 2, -1, -1): 
        dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + num[i][j]

print(dp[n - 1][0])
'''