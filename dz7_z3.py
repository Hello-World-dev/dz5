# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    k = 0

    def __init__(self, k):
        self.k = k

    def __add__(self, other):
        # Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
        # сумме ячеек исходных двух клеток.
        k = self.k + other.k
        c_res = Cell(k)
        return  c_res

    def __sub__(self, other):
        # Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
        # разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
        k = self.k - other.k
        if k < 0:
            print("Разность количества ячеек двух клеток должна быть больше нуля")
        else:
            c_res = Cell(k)
            return c_res

    def __mul__(self, other):
        # Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
        # произведение количества ячеек этих двух клеток.
        k = self.k * other.k
        c_res = Cell(k)
        return c_res

    def __truediv__(self, other):
        # Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
        # целочисленное деление количества ячеек этих двух клеток.
        k = self.k // other.k
        c_res = Cell(k)
        return c_res

c1 = Cell(11)
c2 = Cell(5)

c3 = c1 / c2
print(c3, c3.k)