n, m = list(map(int, input().split()))

print(n, m)

len_n = len(n)
len_m = len(m)

if len_n > len_m:
    print(n, len_n, sep=" ")
elif len_n < len_m:
    print(m, len_m, sep=" ")
else:
    print("same")