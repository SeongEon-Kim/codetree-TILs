n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque

dq = deque()
for i, c in enumerate(cmd):
    if c == "push_back":
        dq.append(num[i])
    elif c == "push_front":
        dq.appendleft(num[i])
    elif c == "pop_front":
        print(dq.popleft())
    elif c == "pop_back":
        print(dq.pop())
    elif c == "size":
        print(len(dq))
    elif c == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif c =="front":
        print(dq[0])
    elif c =="back":
        print(dq[-1])
