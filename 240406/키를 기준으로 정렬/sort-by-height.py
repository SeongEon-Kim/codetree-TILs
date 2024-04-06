# 이름, 키, 몸무게 -> 키 기준 오름차순
class person:
    def __init__(self, name, height, weight):
       self.name = name
       self.height = height
       self.weight = weight

n = int(input())

people = []

for _ in range(n):
    name, height, weight = tuple(map(str, input().split()))
    people.append(person(name, height, weight))

people.sort(key = lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)