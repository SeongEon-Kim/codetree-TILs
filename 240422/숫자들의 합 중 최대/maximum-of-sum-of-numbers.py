x,y = tuple(map(int, input().split()))

ans_list = []
for i in range(x, y+1):
    str_i = str(i)
    ans = 0
    for j in range(len(str_i)):
        ans += int(str_i[j])
    ans_list.append(ans)

print(max(ans_list))