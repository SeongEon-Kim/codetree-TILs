n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

answer = 1
visited = []

# def dfs(vertex):
#     global vertex_cnt
#     for curr_v in range(1, n+1):
#         if graph[vetex][curr_v] and not visited[curr_v]:
#             answer +=1
#             visited[curr_v] = True
#             dfs(curr_v)

# # Please write your code here.
print(n, m, edges)
print(edges[1])

# basic dfs pseudo code
# def dfs(vertex):
#     global vertex_cnt
#     for curr_v in range(1, n+1):
#         if graph[vetex][curr_v] and not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)