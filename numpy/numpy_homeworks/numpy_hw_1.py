import numpy as np
from numpy import random

# Создайте NumPy матрицу 3 на 2, заполните ее единицами.

martix = np.ones((3, 2))
# print(martix)


# Используя NumPy массив X, cоздайте новый NumPy массив такой же размерности и типа, заполненный цифрами 7.
x = np.array([[[8, 3, 16, 2], [14, 7, 12, 0]], [[3, 15, 0, 1], [2, 8, 3, -4]]], dtype='int8')

new_x = np.ones([2, 2, 4], dtype='int8') * 7
# new_x = np.full(x.shape, 7, dtype='int8')
# print(new_x)

# Создайте 3*3*3 NumPy матрицу, заполненную случайными целыми числами в диапазоне от 1 до 10.
random3 = np.random.randint(1, 11, size=(3, 3, 3))
# print(random3)


# Создайте NumPy массив нечетных чисел от 1 до 10, расставленных по убыванию.
array1 = np.arange(1, 10, 2)[::-1]
# print(array1)


# Создайте 3*3 NumPy матрицу, заполненную числами в диапазоне от 0 до 8.
array2 = np.arange(0, 9).reshape(3, 3)
# print(array2)

# Используя NumPy матрицу X, выведите первые два элемента из первых двух строк.
x = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
# print(x[0][0], x[1][0])

# Используя NumPy матрицу X, замените последнее значение последней сроки на 0.
x = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
x[3][3] = 0
# print(x)


# Используя NumPy массив X, выведите элементы большие, чем среднее значение.
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

def array_mean(array):
    mean = array.mean()
    answer = array[array >= mean]
    print(answer)

# array_mean(X)


# Используя NumPy матрицу X, выведите нечетные числа большие, чем среднее значение, исключая 15.
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])


# тут я психанул и хотел решить это имменно так, так как я когда то изучал отдельно JS и нас мучали этими матрицами итд, и я хотел это решить так))

# def array_mean_odd(array):
#     mean = array.mean()
#     answer = []
#
#     for i in range(array.shape[0]):
#         for j in range(array.shape[1]):
#             if array[i][j] >= mean and array[i][j] % 2 != 0 and array[i][j] != 15:
#                 answer.append(int(array[i][j]))
#
#     print(answer)
#
# array_mean_odd(X)



# тут то что вы ожидали видеть от меня

def array_mean_odd(array):
    mean = array.mean()
    # answer = []

    answer = (array > mean) & (array % 2 != 0) & (array != 15)

    print(array[answer])

array_mean_odd(X)

