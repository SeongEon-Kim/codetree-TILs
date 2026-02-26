# DP
# 큰 문제에 대한 답을 얻기 위해 동일한 문제이지만 크기가 더 작은 문제들을 먼저 해결한 뒤, 결과들을 이용해 큰 문제를 간단하게 해결
# 동일한 계산을 memo라는 배열을 만들어서(초기 -1) 필요시 사용
# 배열의 이름은 보통 dp(Dynamic programming)으로 짓는다.
# ex) 피보나치
'''
# (Memoization: Top Down <-> Tabulation: Bottom up)
# 어떤 방법을 사용해도 문제는 없지만, 특정 문제의 경우 한 방법으로 푸는 것이 더 쉬운 경우가 존재
# 재귀함수 활용 동적계획법
def fibbo(n):
    if memo[n] != -1: # 이미 n번째 값을 구해본 적이 있다면
        return memo[n]# memo에 적힌 값을 반환
    if n <= 2:        # 종료 조건
        momo[n] = 1   # 해당하는 숫자 입력
    else:             # 종료 조건이 아니면
        momo[n] = fibbo(n-1) + fibbo(n-2) # 점화식 활용 후 memo에 저장
    
    return memo[n]    # memo 반환
# 시간 복잡도 O(2^n) -> O(n)
# for문 활용 동적계획법
dp = [0] * MAX_N
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
'''
# Bottom-Up 방식(Tabulation)
'''
MAX_N = 45

n = int(input())
dp = [0] * MAX_N
dp[1] = 1
dp[2] = 1

for i in range(3, n+1): # 1, 2, 3, 4, 5, 6, 7
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
'''

# Top-Down 방식(Memoization)
MAX_N = 45
n = int(input())
memo = [-1] * (MAX_N + 1)

def fibbo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else: 
        memo[n] = fibbo(n-1) + fibbo(n-2)
    return memo[n]

print(fibbo(n))
