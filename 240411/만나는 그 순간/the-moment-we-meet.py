# A, B 각각 N, M번 이동
# A, B 개별적으로 시뮬레이션을 진행하되, 각각의 사람이 매 초마다 어느 위치에 있었는지를 기록해주는 식으로 이 문제를 해결해 볼 수 있습니다.(배열을 적극적으로 활용)

n, m = tuple(map(int, input().split()))

a_moving = [tuple(input().split()) for _ in range(n)]
b_moving = [tuple(input().split()) for _ in range(m)]

a_list = []
b_list = []

moving = 0
for idx in range(n):
    if a_moving[idx][0] == 'R':
        for j in range(int(a_moving[idx][1])):
            a_list.append(moving)
            moving += 1 
    else:
        for j in range(int(a_moving[idx][1])):
            a_list.append(moving)
            moving -= 1 

moving = 0
for idx in range(m):
    if b_moving[idx][0] == 'R':
        for j in range(int(b_moving[idx][1])):
            b_list.append(moving)
            moving += 1 
    else:
        for j in range(int(b_moving[idx][1])):
            b_list.append(moving)
            moving -= 1 

for k in range(len(a_list)):
    if k != 0 and a_list[k] == b_list[k]:
        print(k)
        break