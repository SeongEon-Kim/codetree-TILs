def swap(a, b):
    a, b = b, a
    print(a, b, sep=" ")

n, m = tuple(map(int, input().split()))

swap(n, m)