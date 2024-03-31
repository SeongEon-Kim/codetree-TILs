def three_six_nine_contain(i):
    num_str = str(i)
    for digit in num_str:
        if digit in ['3', '6', '9']:
            return True
    return False


def is_magic_number(i):
    return i % 3 == 0 or three_six_nine_contain(i)


n, m = tuple(map(int, input().split()))

cnt = 0

for i in range(n, m+1):
    if is_magic_number(i):
        cnt +=1

print(cnt)