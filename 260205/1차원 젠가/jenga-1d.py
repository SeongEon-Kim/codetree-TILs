n = int(input())

array = []
for i in range(n):
    value = int(input())
    array.append(value)

s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))


def delete(s, e):
    delete_array = []
    for delete_index in range(s-1, e, 1): # 삭제할 배열
        delete_array.append(delete_index)
    return delete_array

def jenga(array, s, e): # 1, 1, 5
    temp_array = []
    for index, value in enumerate(array):
        check_array = delete(s, e)
        if index not in check_array:
            temp_array.append(value)
    return temp_array

first_result = jenga(array, s1, e1)
answer = jenga(first_result, s2, e2)

print(len(answer))
for k in answer:
    print(k)
