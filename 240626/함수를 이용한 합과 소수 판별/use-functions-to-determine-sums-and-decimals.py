a, b = list(map(int, input().split()))

def check_unique(n):
    if ((n % 10) + (n // 10)) % 2 == 0:
        for j in range(2, n):
            if n % j == 0:
                return 0   
        return 1  
    return 0

ans = 0
for i in range(a, b + 1):
    ans += check_unique(i)
print(ans)