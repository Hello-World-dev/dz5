# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

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
        v_p_r = self.inventory_volume.get("Printer") + i_p
        v_s_r = self.inventory_volume.get("Scaner") + i_s
        v_x_r = self.inventory_volume.get("Xerox") + i_x
        self.inventory_volume = {"Printer": v_p_r, "Scaner": v_s_r, "Xerox": v_x_r}
        print("Принял технику, стало:")
        print(self.inventory_volume)

    def putput(self, Derartment, p_p, p_s, p_x):
        print("Передачa в", Derartment, "- подразделение компании")
        v_p_r = self.inventory_volume.get("Printer") - p_p
        v_s_r = self.inventory_volume.get("Scaner") - p_s
        v_x_r = self.inventory_volume.get("Xerox") - p_x
        self.inventory_volume = {"Printer": v_p_r, "Scaner": v_s_r, "Xerox": v_x_r}
        print("На складе осталось:")
        print(self.inventory_volume)

W = Warehouse(5, 5, 5)
W.input(100, 100, 100)
W.putput("Бухгалтерия", 5, 4, 1)


