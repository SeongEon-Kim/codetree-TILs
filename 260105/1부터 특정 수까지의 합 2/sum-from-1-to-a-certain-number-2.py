N = int(input())

# Please write your code here.
def sum_1_n(n):
    if n == 1:
        return 1
    return sum_1_n(n-1) + n

print(sum_1_n(N))
    