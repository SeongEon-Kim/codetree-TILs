# 1, 2, 3, [6, 5, 1]
# 1, 1, 2, [3, 6, 5]
# 5, 1, 1, [2, 3, 6]

n, t = tuple(map(int, input().split()))

up_belts = list(map(int, input().split()))
down_belts = list(map(int, input().split()))
full_belts = up_belts + down_belts

for _ in range(t):
    tmp = full_belts[-1]
    for i in range(len(full_belts)-1,0,-1):
        full_belts[i] = full_belts[i-1]
    full_belts[0] = tmp

up_belts = full_belts[:n]
down_belts = full_belts[n:]

for i in up_belts:
    print(i, end=" ")
print()
for i in down_belts:
    print(i, end=" ")

