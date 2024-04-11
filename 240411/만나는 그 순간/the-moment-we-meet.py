# A, B 각각 N, M번 이동
# A, B 개별적으로 시뮬레이션을 진행하되, 각각의 사람이 매 초마다 어느 위치에 있었는지를 기록해주는 식으로 이 문제를 해결해 볼 수 있습니다.(배열을 적극적으로 활용)

n, m = int(input().split())

a_moving = [tuple(input().split()) for _ in range(n)]
b_moving = [tuple(input().split()) for _ in range(m)]

print(a_moving, b_moving)

a_list = []
b_list = []

moving = 1
for idx in range(n):
    if a_moving[idx][0] == 'R':
        for j in range(int(a_moving[idx][1])):
            moving += 1 
            a_list.append(moving)
    else:
        for j in range(int(a_moving[idx][1])):
            moving -= 1 
            a_list.append(moving)

print(a_list)