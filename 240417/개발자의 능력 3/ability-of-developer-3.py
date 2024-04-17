_list = list(map(int, input().split()))

def diff_ability(i, j, k):
    sum1 =  _list[i] + _list[j] + _list[k]
    sum2 = sum(_list) - sum1
    return abs(sum1 - sum2)

min_diff = 1000000
for i in range(len(_list)):
    for j in range(i+1, len(_list)):
        for k in range(j+1, len(_list)):
            min_diff = min(min_diff, diff_ability(i, j, k))

print(min_diff)