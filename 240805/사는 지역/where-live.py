class People:
    def __init__(self, name, zip_code, place):
        self.name = name
        self.zip_code = zip_code
        self.place = place
    def getlivingplace(self):
        print("name", self.name)
        print("addr", self.zip_code)
        print("city", self.place)
        
n = int(input())

_list = [ list(map(str, input().split())) for _ in range(n)]

last_name = 'a'
last_index = 0
for i in range(n):
    if _list[i][0] > last_name:
        last_name = _list[i][0]
        last_index = i

last_people = People(_list[last_index][0], _list[last_index][1], _list[last_index][2])
last_people.getlivingplace()