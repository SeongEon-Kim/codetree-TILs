_list = list(input())

num = 0

for i in range(len(_list)):
    if _list[i] == "(":
        for j in range(i+1, len(_list), 1):
            if _list[j] == ")":
                num += 1
    else: # ")"
        pass
print(num)