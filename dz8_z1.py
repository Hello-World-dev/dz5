# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

day = 0
month = 0
year = 0000

class Data:
    #day = 0
    #month = 0
    #year = 0000
    im_dat = "00-00-0000"

    def __init__(self, im_dat):
        self.im_dat = im_dat

    @classmethod
    def to_int(cls, s: str):
        day = int(s[0:2])
        #print(day)
        month = int(s[3:5])
        #print(month)
        year = int(s[6:12])
        #print(year)

    @staticmethod
    def valid(v_day, v_month, year):
        if v_day > 31:
            print("invalid day")
        if v_month > 12:
            print("invalid month")

#d = Data("32-05-2005")
Data.to_int("12-05-2021")
#print(day)
Data.valid(day, month, year)

