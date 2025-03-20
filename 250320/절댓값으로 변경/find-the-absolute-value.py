n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abs_value(arr):
    for arr_value in arr:
        if arr_value < 0:
            arr_value = -arr_value
        print(arr_value, end=" ")

abs_value(arr)