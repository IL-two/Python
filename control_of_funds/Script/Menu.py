from Script import cvs_list
from datetime import datetime


def inputDate():
    return str(datetime.strptime(input("Введите дату в формате DD/MM/YYYY: "), "%d/%m/%Y").strftime("%Y-%m-%d"))


class Menu:
    __productList = list()

    def __init__(self):
        self.MainMenu()

    def MainMenu(self):

        self.__productList = cvs_list.readCvsForList()
        while True:
            print("1. Добавить товар\n"
                  "2. Показать все товары\n"
                  "3. Найти по категарии\n"
                  "4. Найти по дате\n"
                  "5. Сортировать по цене (min->max)\n"
                  "6. Удалить товары\n"
                  "0. Выход\n")
            try:
                choice = int(input("Выберите нужный номер пункта: "))

                if choice == 1:
                    prod = {"Category": str(input("Введите имя категории: ")),
                            "Name": str(input("Введите название продукта: ")),
                            "Cost": float(input("Введите стоимость товара: ")),
                            "Date": inputDate()}
                    self.__productList.append(prod)
                    cvs_list.addCvsList(self.__productList)
                elif choice == 2:
                    self.printList()
                elif choice == 3:
                    self.find_by_key(choice)
                elif choice == 4:
                    self.find_by_key(choice)
                elif choice == 5:
                    self.sortListCost()
                elif choice == 6:
                    out = input("Вы уверенны что хотите удалить ВСЕ товары? Y/N ")
                    if out.upper() == 'Y':
                        cvs_list.clearFile()
                        self.__productList.clear()
                        print("Файл отчищен")
                    elif out.upper() == 'N':
                        print("Операция отменена")
                    else:
                        print("Неверный ввод")
                elif choice == 0:
                    break
                else:
                    print("Такого пункта не существует, но возможно мы скоро его добавим")
            except ValueError:
                print("Некоректный ввод")

    # Печать на экран всех товаров
    def printList(self):
        if self.productNull():
            print("Товаров пока нет. Добавте товар.")
        else:
            print("{:<15}{:<15}{:<15}{}".format("Категория:", "Имя:", "Стоимость:", "Дата:"))
            for index, dict_ in enumerate(self.__productList):
                self.printIndex(index)

    # По какой категории конкретно надо искать?
    def find_by_key(self, choice):
        if self.productNull():
            print("Товаров пока нет. Добавте товар.")
        else:
            if choice == 3:
                key = "Category"
                value = input("Введите имя нужной категории: ")
            elif choice == 4:
                key = "Date"
                value = inputDate()
            self.find(key, value)

    # Поиск в соотвествии с категорией
    def find(self, key, value):
        i = -1
        print("{:<15}{:<15}{:<15}{}".format("Категория:", "Имя:", "Стоимость:", "Дата:"))
        for index, dict_ in enumerate(self.__productList):
            if key in dict_ and dict_[key] == value:
                self.printIndex(index)
                i += 1
        if i == -1:
            print("Ничего не найдено")

    # Печать товаров по индексу
    def printIndex(self, index):
        print("{0:<15}{1:<15}{2:<15}{3}".format(self.__productList[index]["Category"],
                                                self.__productList[index]["Name"],
                                                self.__productList[index]["Cost"],
                                                self.__productList[index]["Date"]))

    # Проверка на пустой файл
    def productNull(self):
        return self.__productList is None or len(self.__productList) == 0

    # Сортировка по возвростанию цены
    def sortListCost(self):
        if self.productNull():
            print("Товаров пока нет. Добавте товар.")
        else:
            self.__productList.sort(key=lambda x: float(x["Cost"]))
            self.printList()
            out = input("Сохранить сортированную таблицу в файл? Y/N ")
            # Возможность сохранить отсортированный список
            if out.upper() == 'Y':
                cvs_list.addCvsList(self.__productList)
            elif out.upper() == 'N':
                self.__productList = cvs_list.readCvsForList()
            else:
                self.__productList = cvs_list.readCvsForList()
                print("Неверный ввод")
