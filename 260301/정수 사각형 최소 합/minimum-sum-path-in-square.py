n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INF = 10000000
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