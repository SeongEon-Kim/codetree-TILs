n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

triangle_belt = l + r + d 
# 1 2 4 5 9 3 6 5 1

for _ in range(t): # t초 동안
    temp = triangle_belt[-1] # 1
    for i in range(3*n-1,0,-1): # 1칸씩 이동
        triangle_belt[i] = triangle_belt[i-1]
    triangle_belt[0] = temp
    
for j in range(0,3*n, n):
    for k in range(n):
        print(triangle_belt[k+j], end=" ")
    print()