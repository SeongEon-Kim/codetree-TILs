# 1~n 숫자 중 m개의 숫자를 골라 만들 수 있는 모든 조합을 출력
n, m  = tuple(map(int, input().split()))
answer_list = []

def print_answer():
    for i in answer_list:
        print(i, end=" ")
    print()
def selection_n_of_m(curr_num):
    if curr_num == m +1:
        print_answer()
        return

    for j in range(1, n+1): # 1~n 숫자 중
        if j in answer_list:
            continue
        if len(answer_list)>=1 and max(answer_list) > j:
            continue 
        
        answer_list.append(j)
        selection_n_of_m(curr_num + 1)
        answer_list.pop()


selection_n_of_m(1)


"""

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
combination = []

# 방문한 원소들을 출력해줍니다.
def print_combination():
    for elem in combination:
        print(elem, end = " ")
    print()

def find_combination(curr_num, cnt):
    # n개의 숫자를 모두 탐색햇므녀 더 이상 탐색하지 않는다.
    if curr_num == n+1:
        # 탐색하는 과정에서 m개의 숫자를 뽑은 경우 답을 출력해줍니다.
        if cnt == m:
            print_combination()
        return

    # curr_num에 해당하는 숫자를 사용했을 때의 경우를 탐색합니다. 
    combination.append(curr_num)
    find_combination(curr_num+1, cnt+1)
    combination.pop()

    # curr_num에 해당하는 숫자를 사용하지 않았을 때의 경우를 탐색합니다.
    find_combination(curr_num + 1, cnt)

find_combination(1, 0)
"""

"""
# 이전에 골라진 값을 기준으로 이후의 값들만 순회하기 위해서는 
# 재귀함수의 인자에 마지막으로 뽑은 숫자를 나타낼 값을 추가해줘야만 한다.
# 마지막으로 뽑은 숫자를 나타낼 값을 추가해줘야 한다. find_combination(int cnt, int last_num)
# 지금까지 cnt개의 숫자를 뽑았고, 마지막으로 뽑은 숫자가 last_num일 때, 남은 숫자 중에서 어떤 숫자를 뽑을지 선택

import sys

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
combination = []

def print_combination():
    print(' '.join(map(str, combination)))

# 지금까지 뽑은 개수와 마지막으로 뽑힌 숫자를 추적하여 다음에 뽑힐 수 있는 원소의 후보를 정함
def fine_combination(cnt, last_num):
    # m개를 모두 뽑은 경우 답을 출력
    if cnt == m:
        print_combination()
        return
    
    # 남아있는 수를 모두 골라도 m개를 고를 수 없다면, 탐색을 종료한다.
    if ((n- last_num) < (m-cnt)):
        return
    
    # 뽑을 수 있는 원소의 후보들을 탐색
    for i in range(last_num + 1, n + 1):
        combination.append(i)
        find_combination(cnt+1, i)
        combination.pop()
    
    # 가능한 범위를 순회하며 해당 숫자가 조합의 첫번째 숫자일 대를 탐색
for i in range(1, n+1):
    combination.append(i)
    find_combination(1, i)
    combination.pop()