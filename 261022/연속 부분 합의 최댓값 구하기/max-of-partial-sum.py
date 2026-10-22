n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

def initialize():
    dp[0] = arr[0]

initialize()

# dp[i]: arr[i]에서 끝나는 연속 부분 수열의 최대 합
for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))