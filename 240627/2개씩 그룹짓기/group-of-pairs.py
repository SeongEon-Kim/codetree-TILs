n = int(input())

_list = list(map(int, input().split()))

_list.sort()

ans = []
for idx in range(len(_list)//2):
    ans.append(_list[idx] + _list[-idx-1])

print(max(ans))