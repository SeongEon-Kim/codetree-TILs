A = input()

answer_list =[]
for i in A:
    answer_list.append(i)
if len(set(answer_list)) >= 2:
    print("Yes")
else:
    print("No")
