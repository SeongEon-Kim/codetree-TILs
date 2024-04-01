def is_palindrome(a):
    for i in range(len(a) // 2):
        if a[i] != a[-(i + 1)]:
            return "No"
    return "Yes"

n = input()

print(is_palindrome(n))