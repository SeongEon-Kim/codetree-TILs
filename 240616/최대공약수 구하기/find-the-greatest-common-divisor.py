n, m = list(map(int, input().split()))

def max_conum(n, m):
    min_num = min(n, m) 
    for idx in range(min_num, 0, -1): 
        if n % idx == 0 and m % idx == 0:
            return idx  
    return 1  

print(max_conum(n, m))