# 시간초과가 발생하는 정답 코드(Backtracking 활용)
'''
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dx, dy = [1,0], [0,1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def recur(x,y):
    if x == n-1 and y == n-1 :
        return arr[n-1][n-1]

    max_value = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue
        
        max_value = max(max_value, recur(nx, ny) + arr[x][y])
    return max_value

print(recur(0,0))
'''

# DP 활용 (Topdown)
# 시간초과가 발생하는 정답 코드(Backtracking 활용)
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dx, dy = [1,0], [0,1]
dp = [[-1 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n


def recur(x,y):
    if x == n-1 and y == n-1 :
        return arr[n-1][n-1]

    if dp[x][y] != -1:
        return dp[x][y]
    
    max_value = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue
        
        max_value = max(max_value, recur(nx, ny) + arr[x][y])
    
    dp[x][y] = max_value
    return dp[x][y]

print(recur(0,0))

# 특정 상태의 답이 결정적이어야함(변하지 않아야) 함
# 이전 상태에서 다음 상태의 값이 나올 수 있어야한다(확장 가능해야한다) -> 작은 문제들의 답으로 큰 문제를 풀 수 있어야 한다.

# > k층에 도달했을 때 얻을 수 있는 최대 합
# 2. 1층부터 ... k-1층까지 도달했을 때 얻을 수 있는 최대합을 알면 k층에 도달했을 때 얻을 수 있는 최대합을 구할 수 있는가?
# k, j = max((k-1, j-1), (k-1, j)) + input[k][j]

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0]*n for _ in range(n)]

# dp[0][0] = grid[0][0]

# # 첫 행(오른쪽으로만)
# for j in range(1, n):
#     dp[0][j] = dp[0][j-1] + grid[0][j]

# # 첫 열(아래로만)
# for i in range(1, n):
#     dp[i][0] = dp[i-1][0] + grid[i][0]

# # 나머지
# for i in range(1, n):
#     for j in range(1, n):
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# print(dp[n-1][n-1])