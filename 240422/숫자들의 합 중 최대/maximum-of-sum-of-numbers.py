x,y = tuple(map(int, input().split()))

ans = []
for i in range(x, y+1):
    a = i % 10
    b = i // 10
    ans.append(a+b)

print(max(ans))