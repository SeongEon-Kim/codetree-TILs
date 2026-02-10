k, n = tuple(map(int, input().split()))
answer = []

def print_ans():
    for i in answer:
        print(i, end = " ")
    print()

def selection(curr_num): # 1~n번째
    if curr_num == n + 1:
        print_ans()
        return
    
    for j in range(1, k+1):
        if len(answer) >= 2 and answer[-1] == answer[-2] == j:
            continue
        
        answer.append(j)
        selection(curr_num+1)
        answer.pop()

selection(1)
