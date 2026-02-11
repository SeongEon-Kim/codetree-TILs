# 아름다운수: 1~4의 정수 / 
# 등장했다면 해당 숫자만큼 연달아 나와야함 ex: 133221 / 
# 동일한 숫자에 대해 연달아 같은 숫자 묶음이 나오는 것 또한 아름다운 수 ex: 111 <-> 222 (2 2번, 2 1번)

n = int(input())
n = 1234
input_list = []

while True:
    if n < 10:
        input_list.append(n) # 나머지 넣기(뒷자리)
        break
    a = n % 10 # 나머지
    n = n // 10 # 몫
    input_list.append(a) # 나머지 넣기(뒷자리)

input_list = input_list[::-1]
print(input_list)