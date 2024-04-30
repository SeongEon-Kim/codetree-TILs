def push_back(value):
    ans_list.append(value)

def pop_back():
    del ans_list[-1]

def size():
    print(len(ans_list))

def get(value):
    print(ans_list[value-1])

n = int(input())
_list = []

for _ in range(n):
    command = input().split()
    _list.append(command)

ans_list = []

for idx in range(n):
    if _list[idx][0]=="push_back":
        push_back(int(_list[idx][1]))
    elif _list[idx][0]=="pop_back":
        pop_back()
    elif _list[idx][0]=="size":
        size()
    else:
        get(int(_list[idx][1]))