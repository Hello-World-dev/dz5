# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Office_Equipment:
    paper_format = ""

    def __init__(self, q, p = "A4"):
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


class Warehouse():
    inventory_volume = {} #"wage": 50, "bonus": 30}

    def __init__(self, v_p, v_s, v_x):
        self.inventory_volume = {"Printer": v_p, "Scaner": v_s, "Xerox": v_x}
        print(self.inventory_volume)

    def input(self, i_p, i_s, i_x):
        try:
            a = int(i_p)
            a = int(i_s)
            a = int(i_x)
            if not i_s.is_integer() or not i_p.is_integer() or not i_x.is_integer():
                raise OwnError("Оргтехника не может быть не целой")
        except ValueError:
            print("На склад может быть принято только целое число единиц техники")
        except OwnError as err:
            print(err)
        else:
            v_p_r = self.inventory_volume.get("Printer") + i_p
            v_s_r = self.inventory_volume.get("Scaner") + i_s
            v_x_r = self.inventory_volume.get("Xerox") + i_x
            self.inventory_volume = {"Printer": v_p_r, "Scaner": v_s_r, "Xerox": v_x_r}
            print("Принял технику, стало:")
            print(self.inventory_volume)

    def putput(self, Derartment, p_p, p_s, p_x):
        print("Передачa в", Derartment, "- подразделение компании")
        try:
            a = int(p_p)
            a = int(p_s)
            a = int(p_x)
            if not p_s.is_integer():
                raise OwnError("Оргтехника не может быть не целой")
            if not p_p.is_integer():
                raise OwnError("Оргтехника не может быть не целой")
            if not p_x.is_integer():
                raise OwnError("Оргтехника не может быть не целой")
        except ValueError:
            print("Со склада может быть отгружено только целое число единиц техники")
        except OwnError as err:
            print(err)
        except AttributeError:
            print("test")
        else:
            v_p_r = self.inventory_volume.get("Printer") - p_p
            v_s_r = self.inventory_volume.get("Scaner") - p_s
            v_x_r = self.inventory_volume.get("Xerox") - p_x
            self.inventory_volume = {"Printer": v_p_r, "Scaner": v_s_r, "Xerox": v_x_r}
            print("На складе осталось:")
            print(self.inventory_volume)

W = Warehouse(5, 5, 5)

W.input("r", 100, 100)
W.putput("Бухгалтерия", 5, 4.46, 1)
W.input(55, 100.3409, 100)

W.putput("Бухгалтерия", 1, 1, 1)

print(W.inventory_volume)

