def star_recursion(n):
    if n == 0:
        return
    star_recursion(n-1)
    print("*"*n)

n = int(input())
star_recursion(n)