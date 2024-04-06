n, k = tuple(map(int, input().split()))

block_setting = [0 for _ in range(n)]

block = [list(map(int, input().split())) for _ in range(k)]

for idx in range(k):
    if block[idx][0] == block[idx][1]:
        block_setting[block[idx][0]-1] += 1
    else:
        for j in range(block[idx][0]-1, block[idx][1]):
            block_setting[j] +=1

print(max(block_setting))