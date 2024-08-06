m, d = tuple(map(int, input().split()))

if m in [4, 6, 9, 11]:
    if d <= 30:
        print('Yes')
    else:
        print('No')
elif m in [1, 3, 5, 7, 8, 10, 12]:
    if d <= 31:
        print('Yes')
    else:
        print('No')
elif m in [2]:
    if d <= 28:
        print('Yes')
    else:
        print('No')