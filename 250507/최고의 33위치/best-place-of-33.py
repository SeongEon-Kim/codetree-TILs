n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def get_num_of_gold(row_s, col_s):
    gold_count = 0 
    row_e = row_s + 3
    col_e = col_s + 3
    for i in range(row_s, row_e):
        for j in range(col_s, col_e):
            gold_count += grid[i][j]
    return gold_count

max_gold = 0

for k in range((n-3)+1):
    for l in range((n-3)+1):
        temp_gold = get_num_of_gold(k,l)
        if temp_gold > max_gold:
            max_gold = temp_gold
print(max_gold)