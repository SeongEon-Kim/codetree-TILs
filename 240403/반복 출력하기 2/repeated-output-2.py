def hellowolrd_print(n):
    if n == 0:
        return
    hellowolrd_print(n-1) 
    print("HelloWorld")

n = int(input())
hellowolrd_print(n)