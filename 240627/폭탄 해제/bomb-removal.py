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