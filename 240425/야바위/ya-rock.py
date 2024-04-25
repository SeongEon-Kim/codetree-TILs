n = int(input())
_list = [list(map(int,input().split())) for _ in range(n)]

score_list = []
for i in range(3):
    score = 0
    if i == 0:
        ans_list = [1, 0, 0]
    elif i == 1:
        ans_list = [0, 1, 0]
    else:
        ans_list = [0, 0, 1]
    for j in range(n):
        a = _list[j][0]-1
        b = _list[j][1]-1
        c = _list[j][2]-1
        
        tmp_val = ans_list[a]
        ans_list[a] = ans_list[b]
        ans_list[b] = tmp_val
        if ans_list[c] == 1:

            score +=1
    score_list.append(score)

print(max(score_list))