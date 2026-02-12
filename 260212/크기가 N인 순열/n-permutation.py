n = int(input())
answer_list = []
visited = [False] * (n+1)

def print_ans():
    for elem in answer_list:
        print(elem, end = " ")
    print()

def permutation(curr_num):
    if curr_num == n+1:
        print_ans()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer_list.append(i)
        
        permutation(curr_num+1)
        
        answer_list.pop()
        visited[i] = False

permutation(1)