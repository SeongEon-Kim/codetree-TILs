n = int(input())
_list = list(map(int, input().split()))

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n, 1):
        if _list[j] < _list[min_idx]:
            min_idx = j
    tmp = _list[i]
    _list[i] = _list[min_idx]
    _list[min_idx] = tmp

for k in range(n):
    print(_list[k], end= " ")

#     function selection_sort(arr[])
#   set len = arr.size
#   for i = 0 ... i < len-1
#     set min = i
#     for j = i+1 ... j < len
#       if arr[j] < arr[min]
#         (1)
#     set tmp = arr[i]
#     arr[i] = (2)
#     (3) = tmp
  
#   return arr