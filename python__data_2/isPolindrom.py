def isPolindrom():
    word = input('Введите слово, и я проверю является ли оно палиндромом: ').strip().lower()
    if word[::-1] == word:
        print(True)
    else:
        print(False)

isPolindrom()