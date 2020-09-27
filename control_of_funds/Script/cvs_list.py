import csv

fileName = "../control_of_funds.csv"


# Запись в файл
def addCvsList(product_list):
    with open(fileName, "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(product_list[0].keys()))
        writer.writeheader()
        for row in product_list:
            writer.writerow(row)
    print("Выполнено")
    file.close()


# Чтение файла
def readCvsForList():
    try:
        with open(fileName, 'r') as read_obj:
            dict_reader = csv.DictReader(read_obj)
            list_of_dict = list(dict_reader)
        return list_of_dict
    except FileNotFoundError:
        print("Добро пожаловать!")
        file = open(fileName, 'w')
        file.close()
        return list()


# Отчистка файла
def clearFile():
    try:
        file = open(fileName, 'w')
        file.close()
    except FileNotFoundError:
        print("Файл отсутствует")
