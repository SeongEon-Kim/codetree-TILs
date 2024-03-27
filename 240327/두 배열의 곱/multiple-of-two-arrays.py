first_2d = [ list(map(int,input().split())) for _ in range(3)]
space = list(map(int,input().split())) # 풀이 이후, 다른 방법 찾기
second_2d = [ list(map(int,input().split())) for _ in range(3)]

print(first_2d, second_2d)
for i range(3):
    for j range(3):
        print(first_2d[i][j]*second_2d[i][j], end = " ")
    print()