N = int(input())

# Please write your code here.
def until_one(N):
    if N == 1:
        return 0
    if N % 2 == 0:
        return until_one(N//2) + 1
    else :
        return until_one(N//3) + 1

print(until_one(N))