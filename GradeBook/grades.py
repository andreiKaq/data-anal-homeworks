import json
import database

def add_student(name, data):
    if str(name):
        data[name] = []

        database.save_data(data)

        print('Студент добавлен!')
    else:
        print('Введите имя студента коректно! Пример: ИМЯ ФАМИЛИЯ. ')

def add_grade(name, grade, data):
    student_found = False
    if name in data:
        data[name].append(int(grade))
        student_found = True

    if student_found:
        database.save_data(data)
        print('Оценка добавлена!')
    else:
        print('Студент не найден!')

def view_students(data):
    for student, grades in data.items():
        if grades:
            avg_grades = sum(grades) / len(grades)
            print(student, avg_grades)

def find_best_student(data):
    best_student = None

    for student, grades in data.items():
        if grades:
            avg_grades = sum(grades) / len(grades)
            if best_student is None or avg_grades > best_student[1]:
                best_student = (student, avg_grades)

    if best_student:
        print(f"Лучший студент: {best_student[0]} с средним балом {best_student[1]}")
    else:
        print('Нету студентов с оценками!')

def find_worst_student(data):
    worst_student = None

    for student, grades in data.items():
        if grades:
            avg_grades = sum(grades) / len(grades)
            if worst_student is None or avg_grades < worst_student[1]:
                worst_student = (student, avg_grades)

    if worst_student:
        print(f"Худший студент: {worst_student[0]} с средним балом {worst_student[1]}")
    else:
        print('Нету студентов с оценками!')

def find_student(name, data):
    students = data
    for student, grades in students.items():
        if grades:
            avg_grade = sum(grades) / len(grades)
            if name == student:
                print(name, avg_grade)


def remove_grades(name, data):
    students = data
    if name in students:
        students[name] = []
    print(f'Оценки студента {name} были успешно удалены!')

def remove_student(name, data):
    students = data
    if name in students:
        del students[name]

    print('Студент удален!')