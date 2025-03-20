n, k, t = input().split()
n, k = int(n), int(k)
string_list = [input() for _ in range(n)]

# Please write your code here.
include_list = []
for string in string_list:
    if t in string:
        include_list.append(string)

print(include_list[k-1])