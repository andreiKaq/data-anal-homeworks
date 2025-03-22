def main():
    print("\033[92m")

    print('Добро пожаловать в простой калькулятор!')
    first_num = int(input('Введите число/цыфру: '))
    operator = input('Введите символ + для сложения, - для вычетания, * для умножения, / для деления: ')
    second_num = int(input('Введите число/цыфру: '))


    if operator == '+':
        answer = first_num + second_num
    elif operator == '-':
        answer = first_num - second_num
    elif operator == '*':
        answer = first_num * second_num
    elif operator == '/':
        answer = first_num / second_num
    else:
        answer = 'введите только доступные операторы!'

    print(answer)

main()