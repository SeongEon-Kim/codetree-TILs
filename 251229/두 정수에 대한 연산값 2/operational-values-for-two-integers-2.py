a, b = map(int, input().split())

# Please write your code here.
# 작은 수엔 10 더하고, 큰 수엔 2 곱하기

def compute_two_integer(a, b):
    if a > b:
        print(2*a, b+10)
    else:
        print(a+10, 2*b)

compute_two_integer(a, b)