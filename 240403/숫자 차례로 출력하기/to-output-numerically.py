def upper(n): # 7 6 5 4 3 2 1
    if n == 0 :
        return
    upper(n-1) # 6 5 4 3 2 1 0
    print(n, end = " ")

def lower(n):
    if n == 0:
        return
    print(n, end = " ")
    lower(n-1)

n = int(input())

upper(n)
print()
lower(n)