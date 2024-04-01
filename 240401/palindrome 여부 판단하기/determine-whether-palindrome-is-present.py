def is_palinadrome(a):
    for i in range(len(a)):
        if a[i] == a[len(a)-(i+1)]:
            status = True
        else:
            status = False
            break
    if status:
        print("Yes")
    else:
        print("No")

#    else : # 홀수
        # for i in range(len(a)):
        #     if a[i] == a[len(a)-(i+1)]:
        #         status = True
        # if status:
        #     print("Yes")
        # else:
        #     print("No")


n = str(input().split())

is_palinadrome(n)