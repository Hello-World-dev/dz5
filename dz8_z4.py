# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:

    def input(self):
        print("Принял технику")

    def putput(self):
        print("Отгрузил технику")

class Office_Equipment:
    quantity = 0
    paper_format = ""

    def __init__(self, q, p = "A4"):
        self.quantity = q
        self.paper_format = p


class Printer(Office_Equipment):
    color = False

    def Printer_is_Color(self):
        self.color = True

class Scaner(Office_Equipment):
    Brand = ""

    def set_Brand(self, b):
        self.Brand = b

class Xerox(Office_Equipment):
    year_of_release = 1900

pr1 = Printer(1, "A5")
pr1.Printer_is_Color()
#print(pr1.color)
#print(pr1.paper_format)

s1 = Scaner(1, "A3")
s1.set_Brand("Canon")

x1 = Xerox(1)
x1.year_of_release = 2019
print(x1.year_of_release)