n = 5

basic_arr = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i >= 1 and j >=1 :
            basic_arr[i][j] = basic_arr[i-1][j] + basic_arr[i][j-1]
        
for i in range(n):
    for j in range(n):
        print(basic_arr[i][j], end=" ") 
    print()