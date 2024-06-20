student_data = {
    1 : "John",
    2 : "Tom",
    3 : "Paul"
}

n = int(input())

if n == 1:
    print(student_data[1])
elif n == 2:
    print(student_data[2])
elif n == 3:
    print(student_data[3])
else:
    print("Vacancy")