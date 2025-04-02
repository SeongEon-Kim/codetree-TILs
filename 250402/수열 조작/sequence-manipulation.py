from collections import deque
n = int(input())

# Please write your code here.
# 1 2 3 4 5 6 7 pop_left, push(pop_left)
# 3 4 5 6 7 2 pop_left, push(pop_left)
# 5 6 7 2 4 pop_left, push(pop_left)
# if size(dq)==1: print it

num_list = [i+1 for i in range(n)]

dq = deque()
for v in num_list:
    dq.append(v)

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0]) 
