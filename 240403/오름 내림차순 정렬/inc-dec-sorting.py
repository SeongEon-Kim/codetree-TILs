n = int(input())
m = list(map(int, input().split()))

m.sort()
for i in m:
    print(i, end =" ")

print()

m.sort(reverse=True)
for i in m:
    print(i, end =" ")