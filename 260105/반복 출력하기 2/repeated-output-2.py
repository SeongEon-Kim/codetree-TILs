n = int(input())

# Please write your code here.
def print_helloword(n):
    if n == 0:
        return
    print_helloword(n-1)
    print("HelloWorld")

print_helloword(n)