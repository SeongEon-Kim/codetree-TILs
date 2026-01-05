n = int(input())

# Please write your code here.
def star_print(n):
    if n == 0:
        return
    star_print(n-1)
    print("*"*n)

star_print(n)