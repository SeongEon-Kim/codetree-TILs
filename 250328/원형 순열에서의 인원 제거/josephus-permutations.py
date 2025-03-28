n, k = map(int, input().split())

# Please write your code here.
from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        # 비었으면 처리
        return self.dq.popleft()
    
    def front(self):
        # 비었으면 처리
        return self.dq[0]

q = Queue()
answer = []
for i in range(n):
    q.push(i+1)

# 1명 남을 때 까지 
# 1 2 3 4 5 6 들어감
while q.size() != 0:
    for delete_person in range(k-1):
        # 4 5 6 1 2 3 만들고 4 제거
        q.push(q.front())
        q.pop()
    answer.append(q.front()) # 정답 기록
    q.pop() # 4 제거

for a in answer:
    print(a, end=" ")