# Контрольное задание 1_4B
# От Духно Ильи гр.124/20

import csv

filenameR = "orderdata_sample.csv"
filenameW = "data_total.csv"
quantity = []
price = []
freight = []
total = []

# Чтение из файла
with open(filenameR, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for line in reader:
        quantity.append(line["Quantity"])
        price.append(line["Price"])
        freight.append(line["Freight"])

for i in range(len(quantity)):
    total.append(("total", (float(quantity[i]) * float(price[i]) + float(freight[i]))))

# print(quantity)
# print(price)
# print(freight)
print(total)

# Запись в файл
with open(filenameW, "w", encoding="utf-8", newline="") as fh:
   writer = csv.DictWriter(fh, fieldnames=["total"], quoting=csv.QUOTE_ALL)
#   writer.writeheader()
   for name in total:
        writer.writerow(dict(total=name))