n = int(input())

_list = [int(input()) for _ in range(n)]

same_num = 0
same_num_list = []
for idx in range(n):
    if idx == 0 or _list[idx] == _list[idx-1]:
        same_num += 1
        same_num_list.append(same_num)
    else:
        same_num = 1
        same_num_list.append(same_num)

if max(same_num_list) == 1:
    print(min(same_num_list))
else:
    print(max(same_num_list))