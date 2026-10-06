k, n = tuple(map(int, input().split()))
depth = 0
arr = [[0] for _ in range(n)]

# 2, 0
def recur(k, depth):
    if depth == n:
        print(*arr)
        return
    for i in range(k):
        arr[depth] = i + 1
        recur(k, depth+1)

recur(k, 0)


# n자리 m진수 == 길이 m인 수열에서 n개 고르기
# 1번 템플릿 (중복 순열)
'''
def recur(depth):
    if depth == n:
        print(*arr)
        return
    for i in range(m):
        arr[depth] = i
        recur(depth+1)
'''
# 2번 템플릿 (순열)
'''
visited [False] * m
def recur(depth):
    if depth == n:
        print(*arr)
        return
    
    for i in range(m):
        if visited[i]:
            continue

        arr[depth] = i
        visited[i] = True # 사용중
        recur(depth + 1)
        visited[i] = False
'''
# 3번 템플릿 (조합)
'''
def recur(depth, start):
    if depth == n:
        print(*arr)
        return
    for i in range(start, m):
        arr[depth] = i
        recur(depth + 1, i + 1)
recur(0, 0)
''' 

# k, n = tuple(map(int, input().split()))
# answer = []

# def print_answer(answer):
#     for j in answer:
#         print(j, end=" ")
#     print()

# def selection(pos):
#     global answer
#     if pos == n:
#         print_answer(answer)
#         return
    
#     for i in range(1, k+1):
#         answer.append(i)
#         selection(pos + 1)
#         answer.pop()

# selection(0)

'''
# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return
    
    # 1부터 k까지의 각 숫자가 뽑혔을 때의 경우를 탐색합니다.
    for i in range(1, k + 1):
        selected_nums.append(i)
        find_permutations(cnt + 1)
        selected_nums.pop()


find_permutations(0)
'''