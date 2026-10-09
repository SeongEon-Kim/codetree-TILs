# Bottomup 풀이를 추천하고 싶지 않지만 알아두면 좋은 예시들
# LIS, LCS, 배낭
# DP 역추적 (BFS와 동일한 방식, DP가 어떻게 나온거지?)은 꼭 공부해야한다! 

# 1. Backtracking

# 2. DP - Bottomup
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        
        dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

