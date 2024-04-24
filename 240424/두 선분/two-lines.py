x1, x2, x3, x4 = tuple(map(int, input().split()))

line1 = []
line2 = []
for i in range(x1, x2+1):
    line1.append(i)

for j in range(x3, x4+1):
    line2.append(j)

if x1 in line2:
    print("intersecting")
elif x2 in line2:
    print("intersecting")
elif x3 in line1:
    print("intersecting")
elif x4 in line1:
    print("intersecting")
else:
    print("nonintersecting")