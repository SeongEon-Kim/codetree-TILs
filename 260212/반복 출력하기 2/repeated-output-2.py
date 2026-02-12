n = int(input())

def print_helloworld(curr_n):
    if curr_n == n+1:
        return
    
    print("HelloWorld")
    print_helloworld(curr_n+1)

print_helloworld(1)