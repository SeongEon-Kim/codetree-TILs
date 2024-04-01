def divison_even(_list):
    for i in range(len(_list)):
        if _list[i] % 2 == 0:
            _list[i] = _list[i] // 2
        else:
            pass
    
n = input().split()

_list = list(map(int, input().split()))

divison_even(_list)

for i in _list:
    print(i, end=" ")