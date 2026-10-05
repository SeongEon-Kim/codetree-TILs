n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
ans = 0

def get_coins(i, j):
    coins = 0
    for k in range(i, i+3, 1):
        for l in range(j, j+3, 1):
            if arr[k][l] == 1:
                coins += 1
    return coins

# 3 -> 0 / 4 -> 0, 1 / 5 -> 0, 1, 2 / n -> 0, 1, 2, ... n - 2
for i in range(0, n-2, 1):
    for j in range(0, n-2, 1):
        ans = max(ans, get_coins(i, j))
print(ans)