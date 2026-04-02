n = int(input())
input_list = list(map(int, input().split()))

merged_list = [0] * n

def merge_sort(input_list, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(input_list, low, mid)
        merge_sort(input_list, mid + 1, high)
        merge(input_list, low, mid, high)

def merge(input_list, low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if input_list[i] <= input_list[j]:
            merged_list[k] = input_list[i]
            i += 1
        else:
            merged_list[k] = input_list[j]
            j += 1
        k += 1

    while i <= mid:
        merged_list[k] = input_list[i]
        i += 1
        k += 1

    while j <= high:
        merged_list[k] = input_list[j]
        j += 1
        k += 1

    for p in range(low, high + 1):
        input_list[p] = merged_list[p]

merge_sort(input_list, 0, n - 1)

for i in input_list:
    print(i, end = " ")