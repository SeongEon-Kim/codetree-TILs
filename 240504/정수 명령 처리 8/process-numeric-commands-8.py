class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.node_num += 1

    def pop_front(self):
        if not self.head:
            print("List is empty")
            return
        result = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.node_num -= 1
        print(result)

    def pop_back(self):
        if not self.tail:
            print("List is empty")
            return
        result = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.node_num -= 1
        print(result)

    def size(self):
        print(self.node_num)

    def empty(self):
        print(1 if self.node_num == 0 else 0)

    def front(self):
        if not self.head:
            print("List is empty")
        else:
            print(self.head.data)

    def back(self):
        if not self.tail:
            print("List is empty")
        else:
            print(self.tail.data)

# 입력 처리 부분
DLL = DoublyLinkedList()
n = int(input())

for _ in range(n):
    command, *value = input().split()
    if command == "push_back":
        DLL.push_back(int(value[0]))
    elif command == "push_front":
        DLL.push_front(int(value[0]))
    elif command == "front":
        DLL.front()
    elif command == "back":
        DLL.back()
    elif command == "pop_back":
        DLL.pop_back()
    elif command == "pop_front":
        DLL.pop_front()
    elif command == "empty":
        DLL.empty()
    elif command == "size":
        DLL.size()