code, color, second = list(map(str, input().split()))

class boom():
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
    def print_code():
        print("code :", code)

    def print_color():
        print("color :", color)

    def print_second():
        print("second :", second)

boom(code, color, second)

boom.print_code()
boom.print_color()
boom.print_second()


# # 클래스 선언
# class Bomb:
# 	def __init__(self, unlock_code, linear_color, time):
# 		self.unlock_code = unlock_code
# 		self.linear_color = linear_color
# 		self.time = time

# # 변수 선언 및 입력
# u_code, l_color, time = tuple(input().split())

# # 객체 생성
# b = Bomb(u_code, l_color, int(time))

# # 출력
# print(f"code : {b.unlock_code}")
# print(f"color : {b.linear_color}")
# print(f"second : {b.time}")