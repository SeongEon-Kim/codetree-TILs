N = int(input())
records = list(input())

def solve():
    if N % 2 == 1:
        return "No"

    # '?' 중 '('로 바꿔야 하는 개수
    need_open = N // 2 - records.count("(") 

    if need_open < 0 or need_open > records.count("?"):
        return "No"

    count = 0

    for ch in records:
        if ch == "?":
            if need_open > 0:
                ch = "("
                need_open -= 1
            else:
                ch = ")"

        if ch == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return "No"

    if count == 0:
        return "Yes"
    else:
        return "No"

print(solve())