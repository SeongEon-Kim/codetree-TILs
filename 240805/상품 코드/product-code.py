class product:
    def __init__(self, length, code):
        self.length = length
        self.code = code
    def initialization(self):
        print("product", 50, "is", "codetree")
    def program(self):
        self.initialization()
        print("product", self.code, "is", self.length)
    
code, name = input().split()
structure = product(code, name)
structure.program()