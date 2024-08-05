n1, n2 = tuple(map(int, input().split()))

_list1 = list(map(int, input().split()))
_list2 = list(map(int, input().split()))

status = False
for i in _list1:
    if i in _list2:
        status = True

if status:
    print('Yes')