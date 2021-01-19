# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("f5.txt", "w") as f:
    for i in range(1, 21):
        s = str(randint(1, 50)) + " "
        f.write(s)

with open("f5.txt", "r") as f:
    s = f.read()
    list = s.split()
    res = 0
    for i in list:
        res += int(i)

print(res)
