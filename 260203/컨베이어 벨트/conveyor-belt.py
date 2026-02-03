n, t = tuple(map(int, input().split()))
up_belt = list(map(int, input().split()))
down_belt = list(map(int, input().split()))
belt = up_belt + down_belt
# print(belt) # 1 2 3 / 6 5 1 -> [] 1 1 2 / 3 6 5

temp = belt[2*n-1]
# print(temp)

for i in range(2*n-1,0,-1):
    belt[i] = belt[i-1]
belt[0] = temp 
# print(belt)1 1 2 / 3 6 5

for i in belt[:n]:
    print(i, end=" ")
print()
for j in belt[n:]:
    print(j, end=" ")
