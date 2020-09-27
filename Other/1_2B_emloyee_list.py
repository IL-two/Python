# Контрольное задание 1_2B
# От Духно Ильи гр.124/20


cost = [200, 400, 50, 1200, 500, 1050, 700, 100, 300, 600]
id_eployee = [i for i in range(10)]
product_name = ["Сыр", "Арбуз", "Хлеб", "Колбаса", "Сахар", "Кофе", "Чай", "Молоко", "Курица", "Свинина"]

d = []
for item in range(len(id_eployee)):
    d.append({"Продекут": product_name[item], "Цена": cost[item], "id Продовца": id_eployee[item]})

for item in range(len(d)):
    print(d[item])
