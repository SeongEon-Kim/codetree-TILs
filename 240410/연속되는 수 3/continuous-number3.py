n = int(input())

_list = [int(input()) for _ in range(n)]

ans = []
num = 0

for idx in range(n):
    if idx == 0 or (_list[idx] * _list[idx-1])> 0:
        num += 1
        ans.append(num)
    else:
        num = 1
        ans.append(num)

print(max(ans))