n = 2
arr_2d = [list(map(int, input().split())) for idx in range(n)]
all_sum = 0 

for idx in arr_2d:
    print(sum(idx)/len(idx), end=" ")
print()

for idx in range(len(arr_2d[0])):
    print((arr_2d[0][idx] + arr_2d[1][idx])/2, end=" ")
print()

for idx in arr_2d:
    all_sum += sum(idx)

len_arr_2d = len(arr_2d) * len(arr_2d[0])
all_mean = all_sum/len_arr_2d
print(all_mean)