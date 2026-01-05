N = int(input())

# Please write your code here.
def each_sum_sqared(N):
    if N == 0:
        return 0
    
    return each_sum_sqared(N // 10) + (N %10)**2

print(each_sum_sqared(N))