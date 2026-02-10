k, n = tuple(map(int, input().split()))
answer = []

def print_answer(answer):
    for j in answer:
        print(j, end=" ")
    print()

def selection(pos):
    global answer
    if pos == n:
        print_answer(answer)
        return
    
    for i in range(1, k+1):
        answer.append(i)
        selection(pos + 1)
        answer.pop()

selection(0)
