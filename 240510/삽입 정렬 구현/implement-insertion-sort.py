n = int(input())

_list = list(map(int, input().split()))

def insertion_sort(arr):
    for i in range(n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

_list = insertion_sort(_list)
print(_list, end=' ')