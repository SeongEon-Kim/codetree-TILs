n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

answer = -1

def dfs(vertex):
    global answer
    visited[vertex] = True
    answer += 1

    for curr_v in range(1, n + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            dfs(curr_v)

dfs(1)
print(answer)

# basic dfs pseudo code
# def dfs(vertex):
#     global vertex_cnt
#     for curr_v in range(1, n+1):
#         if graph[vetex][curr_v] and not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)