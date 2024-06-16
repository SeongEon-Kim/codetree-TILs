n, m =list(map(int, input().split()))

def LCP(n, m):
    for idx in range(max(n,m), n*m, 1):
        id n%idx==0 and m%idx==0:
            return idx

print(LCP(n, m))