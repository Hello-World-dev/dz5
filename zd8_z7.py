# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Cmpl:
    val_x = 0.0
    val_y = 0.0

    def __init__(self, x, y ):
        self.val_x = x
        self.val_y = y

    def pr(self):
        c = complex(self.val_x, self.val_y)
        print(c)

    def __add__(self, other):
        c1 = complex(self.val_x, self.val_y)
        c2 = complex(other.val_x, other.val_y)
        c3 = c1 + c2
        return c3

    def __mul__(self, other):
        c1 = complex(self.val_x, self.val_y)
        c2 = complex(other.val_x, other.val_y)
        c3 = c1 * c2
        return c3

c1 = Cmpl(4, 5)
c1.pr()
c2 = Cmpl(-3, -2)
c3 = c1 + c2
print(c3)
c3 = c1 * c2
print(c3)