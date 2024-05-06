n = int(input())
_list = list(map(int, input().split()))

for i in range(n-1):
    for j in range(n-1):
        if _list[j] > _list[j+1]:
            tmp = _list[j]
            _list[j] = _list[j+1]
            _list[j+1] = tmp


for k in range(n):
    print(_list[k], end=" ")