a, b = list(map(int, input().split()))

if a > b:
    print(a*b)
else:
    print(b//a)