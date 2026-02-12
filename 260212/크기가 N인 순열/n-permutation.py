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


"""
# 변수 선언 및 입력:
n = int(input())
visited = [False] * (n + 1)
picked = []


# 지금까지 선택한 수의 개수를 cnt라 했을 때
# 계속 탐색을 이어서 진행합니다.
def get_permutation(cnt):
    # 모든 원소를 선택했을 때, 해당 순열을 출력합니다.
    if cnt == n:
        for elem in picked:
            print(elem, end=" ")
        print()

    # 앞에서부터 하나씩 원소를 선택합니다.
    for i in range(1, n + 1):
        if visited[i]: 
            continue
        
        visited[i] = True
        picked.append(i)

        get_permutation(cnt + 1)

        visited[i] = False
        picked.pop()


get_permutation(0)
"""