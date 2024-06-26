n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b)

if sorted_a == sorted_b:
    print('Yes')
else:
    print('No')