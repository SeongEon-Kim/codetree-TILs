# 특정 상태의 답이 결정적이어야함(변하지 않아야) 함
# 이전 상태에서 다음 상태의 값이 나올 수 있어야한다(확장 가능해야한다) -> 작은 문제들의 답으로 큰 문제를 풀 수 있어야 한다.

# > k층에 도달했을 때 얻을 수 있는 최대 합
# 2. 1층부터 ... k-1층까지 도달했을 때 얻을 수 있는 최대합을 알면 k층에 도달했을 때 얻을 수 있는 최대합을 구할 수 있는가?
# k, j = max((k-1, j-1), (k-1, j)) + input[k][j]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

dp[0][0] = grid[0][0]

# 첫 행(오른쪽으로만)
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# 첫 열(아래로만)
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# 나머지
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[n-1][n-1])