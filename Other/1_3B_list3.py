# Контрольное задание 1_3B
# От Духно Ильи гр.124/20

from random import randint
import csv

lisl1 = [randint(0, 100) for i in range(20)]

print(lisl1)

list2 = ["Больше" for i in lisl1 if i > 50]
list3 = ["Меньше" for i in lisl1 if i < 50]

print(list2)
print(list3)

filename = "input.csv"
list_name = []

# Чтение имен из файла input.csv
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        list_name.append(row[2])

print(list_name)
# print(len(list_name))

list_name_symb = []
list_name_all = []

for item in list_name:
    if item.startswith("M") or item.startswith("A"):
        list_name_symb.append(item)
    else:
        list_name_all.append(item)

print(list_name_symb)
print(list_name_all)