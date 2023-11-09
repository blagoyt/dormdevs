students_grades = {}
n = int(input())
for _ in range(n):
    name, data = tuple([digit for digit in input().split()])
    data = float(data)

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(data)
     if grade > 6:
        print("Invalid grade")
    if grade < 2:
        print("Invalid ")
        continue

for student, datas in sorted(students_grades.items()):
    average_grade = sum(datas) / len(datas)
    formatted_grades = " ".join(map(str, datas))
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")
