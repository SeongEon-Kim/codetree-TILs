n, m = list(map(int,input().split()))

def max_conum(n, m):
    max_num = max(n, m)
    answer = 0
    for idx in range(max_num, 0, -1):
        if max_num%idx==0 and n%idx==0:
            return idx
    
print(max_conum(n, m))