students_grades = {} #Празен речник
n = int(input()) #Въвежда се от конзолата и представлява броя на учениците.
for _ in range(n): # Правим цикъл който се изпълнява n-пъти.
    name, data = tuple([digit for digit in input().split()]) # Въвеждането е първо името после с интервал оценката, и input().split() разделя на списук от низове и после се превръщат в кортеж.
    # name e името на ученика а data е оценката на ученика.
    data = float(data) #превръща ги в реални числа.

    if name not in students_grades:  # Проверяваме дали името на ученика е вече в речника.
        students_grades[name] = []   # Ако не е прави нов запис като списък с стойност.
    students_grades[name].append(data)  # След това добавяме към списъка с името на ученика

for student, datas in sorted(students_grades.items()):  # След това преминава през елементите в речника след сортиране по азбучен ред.
    average_grade = sum(datas) / len(datas)  # За всеки ученик се сметя средната оценка
    formatted_grades = " ".join(map(str, datas))  # След това се форматират с един space разстояние във string-ове с map.
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")  # Принтираме като средната оценка е с 2 знака след десетичната запетая.
