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