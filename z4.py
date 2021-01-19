# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 # Two — 2 # Three — 3 # Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

res_list = []
list = []

with open("f4.txt", "r") as f:
    for line in f:
        #line.replace("One", "Один")
        #print(line)
        list = line.split()
        list[0] = list[0].replace("One", "Один")
        list[0] = list[0].replace("Two", "Два")
        list[0] = list[0].replace("Three", "Три")
        list[0] = list[0].replace("Four", "Четыре")
        res_list.append(list)

#print(res_list)
with open("f4_res.txt", "w", encoding="utf-8") as f:
    for line in res_list:
        str = " ".join(line)
        str += "\n"
        f.write(str)
        #print(str)