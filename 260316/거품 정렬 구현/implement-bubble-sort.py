n = int(input())
input_list = list(map(int, input().split()))

def bubble_sort(input_list):
    for i in range(n-1):
        for j in range(n-1):
            if input_list[j] > input_list[j+1]:
                tmp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = tmp
    return input_list

input_list= bubble_sort(input_list)
for k in input_list:
    print(k, end=" ")