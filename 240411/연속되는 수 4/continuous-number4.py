n = int(input())

_list = [int(input()) for _ in range(n)]

ans = []
continuity = 1

for idx in range(n):
    if idx == 0 or _list[idx-1] < _list[idx]:
        continuity += 1
        ans.append(continuity)
    else:
        continuity = 1
        ans.append(continuity)

print(max(ans))