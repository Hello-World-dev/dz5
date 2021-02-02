# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

import numpy as np

class Matrix:
    ss = [[], []]

    def __init__(self, ss):
        self.ss = ss

    def __str__(self):
        ss = np.array(self.ss)
        return (ss.__str__())

    def __add__(self, other):
        ss1 = np.array(self.ss)
        ss2 = np.array(other.ss)
        ss3 = ss1 + ss2
        return ss3

ss = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = Matrix(ss)
print("Первая матрица :")
print(m1)
ss = [[10, 10, 10], [10, 10, 10], [10, 10, 1000]]
m2 = Matrix(ss)
print("Вторая матрица :")
print(m2)

m3 = m1 + m2
print("Сумма матриц :")
print(m3)

