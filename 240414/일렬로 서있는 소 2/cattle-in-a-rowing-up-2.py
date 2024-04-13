n = int(input())
_list = list(input().split())
print(_list)
num = 0
# 0 2 3, 1 2 3
for i in range(n):
    for j in range(i+1, n, 1):
        for k in range(j+1, n, 1):
            # i <= j <= k 만족
            if (_list[i] <= _list[j]) and (_list[i] <= _list[k]) and (_list[j] <= _list[k]):
                #print(i, j, k)
                #print(_list[i],_list[j],_list[k])
                num +=1

print(num)