def sum_from_input(n):
    sum_value = 0
    for i in range(1, n+1):
        sum_value += i
    return sum_value

n = int(input())

sum_value = sum_from_input(n)

remainer = sum_value // 10
print(remainer)