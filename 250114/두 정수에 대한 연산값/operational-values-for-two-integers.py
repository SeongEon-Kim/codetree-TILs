a, b = map(int, input().split())

# Write your code here!
def calculation(a, b):
    if a < b:
        print(a * 2, b + 25)
    else:
        print(b * 2, a + 25 )
    return

calculation(a,b)