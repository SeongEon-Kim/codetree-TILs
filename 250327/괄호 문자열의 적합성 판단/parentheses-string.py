str = input()

# Please write your code here.
stack = []
for e in str:
    if e =="(":
        stack.append("(")
    else: # )
        stack.pop()

if len(stack) == 0:
    print("Yes")
else: # >0
    print("No")