def is_palinadrome(a):
    for i in range(len(a)):
        if a[i] == a[len(a)-(i+1)]: # 0 1 2 3 
            status = True
        else:
            status = False
            break
    if status:
        print("Yes")
    else:
        print("No")


n = input().split()

is_palinadrome(n)