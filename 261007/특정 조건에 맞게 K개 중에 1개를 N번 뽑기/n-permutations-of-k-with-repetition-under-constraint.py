# 특강 풀이
k, n = tuple(map(int, input().split())) # 2, 3
arr = [0] * n # [0, 0 , 0]

def recur(depth): # 0
    if depth == n: # 0 == 3
        print(*arr)
        return
    
    for i in range(1, k+1): # 1, 2 
        if depth >= 2 and i == arr[depth - 1] and i == arr[depth - 2]:
            continue
        arr[depth] = i # 1 , 1, 
        recur(depth + 1)
    return

recur(0)

# 코드트리 풀이
# k, n = tuple(map(int, input().split()))
# answer = []

# def print_ans():
#     for i in answer:
#         print(i, end = " ")
#     print()

# def selection(curr_num): # 1~n번 뽑기
#     if curr_num == n + 1:
#         print_ans()
#         return
    
#     for j in range(1, k+1): # 1~k 숫자 중에서
#         if len(answer) >= 2 and j == answer[-1] and j == answer[-2]:
#             continue
#         answer.append(j)
#         selection(curr_num+1)
#         answer.pop()
#     return
# selection(1)

# k, n = tuple(map(int, input().split()))
# answer = []

# def print_ans():
#     for i in answer:
#         print(i, end = " ")
#     print()

# def selection(curr_num): # 1~n번째
#     if curr_num == n + 1:
#         print_ans()
#         return
    
#     for j in range(1, k+1):
#         if len(answer) >= 2 and answer[-1] == answer[-2] == j:
#             continue
        
#         answer.append(j)
#         selection(curr_num+1)
#         answer.pop()

# selection(1)

'''
# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_duplicated_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return
    
    for i in range(1, k + 1):
        if cnt >= 2 and i == selected_nums[-1] and \
                        i == selected_nums[-2]:
            continue
        else:
            selected_nums.append(i)
            find_duplicated_permutations(cnt + 1)
            selected_nums.pop()


find_duplicated_permutations(0)
'''