num = int(input())

start_num = 1
for _ in range(num):
    for _ in range(num):
        print(start_num, end=" ")
        start_num+=1
        if start_num == 10:
            start_num = 1
    print()