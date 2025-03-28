from random import choice

import database
import grades
from GradeBook.grades import add_student, add_grade, view_students

data = database.load_data()

while True:
    print("\n--- Менеджер журнала оценок ---")
    print("1. Добавить студента")
    print("2. Добавить оценку")
    print("3. Просмотреть студентов")
    print("4. Найти лучшего студента")
    print("5. Найти худшего студента")
    print("6. Найти студента и увидеть его оценки и средний бал")
    print("7. Выйти")

    choice = input('Выберите опцию от 1 до 6: ')

    if choice == '1':
        name = input("Введите имя студента: ")
        grades.add_student(name, data)

    elif choice == '2':
        name = input("Введите имя студента: ")
        grade = input('Введите оценку студенту: ')
        grades.add_grade(name, grade, data)

    elif choice == '3':
        grades.view_students(data)

    elif choice == '4':
        grades.find_best_student(data)

    elif choice == '5':
        grades.find_worst_student(data)

    elif choice == '6':
        name = input('Выберите студента которого хотите найти: ')
        grades.find_student(name, data)

    elif choice == '7':
        database.save_data(data)
        print('Данный успешно сохранены! До встрчечи!')
        break
    else:
        print('Введите доступную опцию!')














