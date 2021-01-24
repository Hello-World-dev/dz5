# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    _income = {} # "wage": 0, "bonus": 0

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print("Полное имя сотрудника:", self.name, self.surname)

    def get_total_income(self):
        summa = sum(self._income.values())
        print("Доход с учетом премии :", summa)

zp = {"wage": 50, "bonus": 30}
p1 = Position("Ivan", "Petrov", "Boss", zp)
p1.get_full_name()
p1.get_total_income()