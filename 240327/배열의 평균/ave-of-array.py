n = 2
arr_2d = [list(map(int, input().split())) for idx in range(n)]
all_sum = 0 

for idx in arr_2d:
    print(round(sum(idx)/len(idx),1), end=" ")
print()

for idx_1d in range(len(arr_2d[0])):
    sum_length = 0
    for idx_2d in range(len(arr_2d)):
        sum_length += arr_2d[idx_2d][idx_1d]
    print(round(sum_length/len(arr_2d),1), end=" ")
print()

for idx in arr_2d:
    all_sum += sum(idx)

len_arr_2d = len(arr_2d) * len(arr_2d[0])
all_mean = all_sum/len_arr_2d
print(round(all_mean,1))