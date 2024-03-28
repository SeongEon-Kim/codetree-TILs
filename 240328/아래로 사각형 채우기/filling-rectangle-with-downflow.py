n = list(map(int, input().split()))

start = 1

for i in range(n[0]):
    for j in range(n[0]):
        print(start, end=" ")
        start += n[0] 
    print()
    if i ==0:
        start = i + 2
    else: 
        start = i + 1