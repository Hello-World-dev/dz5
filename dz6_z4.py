# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("car go")
    def stop(self):
        print("car stop")
    def turn(self, direction):
        print("car turn")
    def show_speed(self):
        print("Car speed is", self.speed)

class TownCar(Car):
    def show_speed(self):
        print("TownCar speed is", self.speed)
        if self.speed > 60:
            print("Speeding!")

class Workcar(Car):
    def show_speed(self):
        print("Workcar speed is", self.speed)
        if self.speed > 40:
            print("Speeding!")

class Policecar(Car):
    """Police"""
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

class Sportcar(Car):
    """Sport"""

c1 = Car(180, "red", "1", False)
c1.show_speed()
c2 = TownCar(180, "red", "2", False)
c2.show_speed()
c3 = Workcar(180, "red", "1", False)
c3.show_speed()