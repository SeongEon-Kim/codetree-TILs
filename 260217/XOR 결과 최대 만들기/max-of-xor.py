n, m = map(int, input().split())
n_list = list(map(int, input().split()))

answer = []
max_xor = 0

def choose(curr_num, cnt, x):
    global max_xor

    # 가지치기: m개 초과로 뽑으면 불가능
    if cnt > m:
        return

    # 가지치기: 남은 걸 다 뽑아도 m개 못 채우면 불가능
    remaining = n - (curr_num - 1)   # curr_num부터 n까지 남은 개수
    if cnt + remaining < m:
        return

    # 끝까지 결정했으면
    if curr_num == n + 1:
        if cnt == m:
            max_xor = max(max_xor, x)
        return

    # 0: 안 뽑는다
    answer.append(0)
    choose(curr_num + 1, cnt, x)
    answer.pop()

    # 1: 뽑는다 (xor 누적)
    answer.append(1)
    choose(curr_num + 1, cnt + 1, x ^ n_list[curr_num - 1])
    answer.pop()

choose(1, 0, 0)
print(max_xor)