a, b = list(map(int, input().split()))

answer_list = []

def is_prime(n):
    if n==1:
        return 
    for i in range(2, n):
        if n % i == 0: # 소수가 아님
            return 
    answer_list.append(n)
    return

for j in range(a, b+1):
    is_prime(j)

print(sum(answer_list))