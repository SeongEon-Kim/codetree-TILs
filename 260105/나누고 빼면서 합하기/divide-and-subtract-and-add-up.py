n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
# N개의 원소로 이루어진 수열 A가 주어지고, 정수 M이 있다.
# M이 1이 될 때 까지 홀수면 -1, 짝수면 /2 하면서 A의 M번째 원소를 계속 더하기
# 5개의 원소로 이루어진 수열 5 ,4, 3, 2, 1에 대해 4가 1이 될 때 까지
# 짝수 이므로 4 -> 4번째 원소 = idx 3 = 2
# 짝수이므로 2 -> 2번째 원소 = idx 1 = 4 
# 홀수 이므로 1 -> 1번째 원소 = idx 0 = 5

def sol(n, m, A):
    answer = 0
    while m >= 1:
        if m %2 == 0: # 짝수
            answer = answer + A[m-1]
            m = m // 2
        else: # 홀수
            answer = answer + A[m-1]
            m = m -1
    return answer

print(sol(n, m, A))