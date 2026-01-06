n = int(input())
m = list(map(int, input().split()))

def output(m):
    for i in m:
        print(i, end=" ")
    print()

m.sort()
output(m)
m.sort(reverse=True)
output(m)