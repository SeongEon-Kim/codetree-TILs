def three_six_nine_contain(i):
    for j in [3, 6, 9]:
        if i % 10 == j or i // 10 == j:
            return True 

def is_magic_number(i):
    return i % 3 == 0 or three_six_nine_contain(i)


n, m = tuple(map(int, input().split()))

cnt = 0

for i in range(n, m+1):
    if is_magic_number(i):
        cnt +=1

print(cnt)