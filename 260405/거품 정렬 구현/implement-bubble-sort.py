n = int(input())
array = list(map(int, input().split()))

def bubble_sort(array):
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
    
    return array

array = bubble_sort(array)
for k in array:
    print(k, end = " ")