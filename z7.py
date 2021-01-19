#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

sr_pribil = 0.0
spisok = []
with open("f7.txt", "r", encoding="utf-8") as f:
    for line in f:
        pribil = float(line.split()[2]) - float(line.split()[3])
        elem = {line.split()[0]: pribil}
        spisok.append(elem)
        if pribil > 0:
            sr_pribil += pribil
            #print(sr_pribil)
    #print(spisok)

elem = {"average_profit": sr_pribil}
spisok.append(elem)
print(spisok)

with open("f7_res.json", "w", encoding="utf-8") as f:
    json.dump(spisok, f)