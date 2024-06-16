n, m =list(map(int, input().split()))

def LCP(n, m):
    for idx in range(max(n,m), n*m, 1):
        if idx%n==0 and idx%m==0:
            return idx

print(LCP(n, m))