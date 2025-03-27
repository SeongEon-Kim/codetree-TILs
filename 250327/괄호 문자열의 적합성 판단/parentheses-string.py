str = input()

stack = []
is_valid = True

for e in str:
    if e == "(":
        stack.append("(")
    else:  # e == ")"
        if len(stack) > 0:
            stack.pop()
        else:
            is_valid = False
            break

if is_valid and len(stack) == 0:
    print("Yes")
else:
    print("No")
