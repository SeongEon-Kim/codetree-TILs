number = int(input()) 
_list = [input().split() for _ in range(number)]  

answer = 0

for start_row in range(number - 2):  
    for start_col in range(number - 2): 
        current_sum = 0 

        for i in range(3):
            for j in range(3):
                if _list[start_row + i][start_col + j] == "1":
                    current_sum += 1
        answer = max(answer, current_sum)

print(answer)  # 결과 출력