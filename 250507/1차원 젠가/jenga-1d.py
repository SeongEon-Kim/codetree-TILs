n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
# temp1
# temp2
delete_index = []
for k in range(s1-1, e1):
    delete_index.append(k)

temp1 = []
for i, v in enumerate(blocks):
    if i in delete_index:
        pass
    else:
        temp1.append(v)
blocks = temp1


delete_index = []
for l in range(s2-1, e2):
    delete_index.append(l)

temp2 = []
for j, v in enumerate(blocks):
    if j in delete_index:
        pass
    else:
        temp2.append(v)
blocks = temp2
print(len(blocks))

for p in blocks:
    print(p)
