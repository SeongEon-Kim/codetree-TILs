N = int(input())

# Please write your code here.
def each_sum_sqared(N):
    if n == 1:
        return 1
    
    return each_sum_sqared(N%10) + N **2

print(each_sum_sqared(N))