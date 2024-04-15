n = int(input())
arr = list(map(int, input().split()))

max_sum = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] <= arr[j] <= arr[k]:
                max_sum +=1

print(max_sum)