n = int(input())

words = [input() for _ in range(n)]

words.sort()

for idx in range(n):
    print(words[idx])