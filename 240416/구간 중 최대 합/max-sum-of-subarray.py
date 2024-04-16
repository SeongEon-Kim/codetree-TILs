n, k = tuple(map(int, input().split()))
_list = list(map(int, input().split()))

max_sum = 0
for i in range(n-k+1):
    _sum = 0
    for j in range(i, i+k):
        _sum += _list[j]
    max_sum = max(max_sum, _sum)

print(max_sum)