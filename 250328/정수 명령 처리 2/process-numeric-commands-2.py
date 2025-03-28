from collections import deque

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self,item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq

    def size(self):              
        return len(self.dq)
        
    def pop(self):               
        if self.empty():
            raise Exception("Queue is empty")
            
        return self.dq.popleft()
                
    def front(self):             
        if self.empty():
            raise Exception("Queue is empty")
                        
        return self.dq[0]

q = Queue()
for i,c in enumerate(command):
    if c =="push":
        q.push(A[i])
    elif c =="empty":
        print(int(q.empty()))
    elif c=="size":
        print(q.size())
    elif c=="pop":
        print(q.pop())
    else:# front
        print(q.front())