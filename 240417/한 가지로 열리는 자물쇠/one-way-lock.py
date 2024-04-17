n = int(input())
_list = list(map(int, input().split()))

num = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(_list[0]-i) <= 2 or abs(_list[1]-j) <= 2 or abs(_list[2]-k) <= 2:
                num +=1
print(num)