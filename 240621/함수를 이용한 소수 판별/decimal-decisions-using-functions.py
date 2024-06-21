a, b = list(map(int, input().split()))
answer = []

def is_prime(n, a):
    for i in range(2, n): # 소수이면 넣기
        if n % i == 0 and n >= a:
            return False
    return True

for j in range(a, b+1, 1):
    if is_prime(j, a):
        answer.append(j)

print(sum(answer))