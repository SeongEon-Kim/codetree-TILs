class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return 1 if len(self.items) == 0 else 0

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            return -1
        return self.items.pop()

    def top(self):
        if self.empty():
            return -1
        return self.items[-1]

s = Stack()
for i, k in enumerate(command):
    if k == "push":
        s.push(value[i])
    elif k == "empty":
        print(s.empty())
    elif k == "size":
        print(s.size())
    elif k == "pop":
        print(s.pop())
    else:  # top
        print(s.top())
