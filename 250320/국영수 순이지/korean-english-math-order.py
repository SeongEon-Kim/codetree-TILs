n = int(input())
name = []
korean = []
english = []
math = []

students = []

class Student():
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
    students.append(Student(name[-1], korean[-1], english[-1], math[-1]))

# Please write your code here.
# 국 > 영 > 수

students.sort(key = lambda x: (-x.korean, -x.english, -x.math))

for student in students:
    print(student.name, student.korean, student.english, student.math)