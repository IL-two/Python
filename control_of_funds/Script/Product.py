from datetime import datetime


# Попытка сдлеать каждую строку товара объектом

class Product:

    def __init__(self, nameCategory="nameCategory", nameProduct="nameProduct", cost=0.00,
                 date_str=datetime.now().date()):
        self.__nameCategory = nameCategory
        self.__nameProduct = nameProduct
        self.__cost = cost
        self.__date = date_str

    def addProductProp(self, nameCategory, nameProduct, cost, date):
        self.nameCategory = nameCategory
        self.nameProduct = nameProduct
        self.cost = cost
        self.date = date

    @property
    def nameCategory(self):
        return self.__nameCategory

    @nameCategory.setter
    def nameCategory(self, name):
        self.__nameCategory = name

    @property
    def nameProduct(self):
        return self.__nameProduct

    @nameProduct.setter
    def nameProduct(self, name):
        if name is not None:
            self.__nameProduct = name
        else:
            print("Неверное имя")

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        if cost is not None or type(cost) is float:
            self.__cost = cost
        else:
            print("Неверная операция")

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date_str):
        self.__date = self.addDate(date_str)

    def display(self):
        return {"Category": self.nameCategory,
                "Name": self.nameProduct,
                "Cost": self.cost,
                "Date": self.date}

    def addProduct(self):
        try:
            self.nameCategory = str(input("Введите имя категории: "))
            self.nameProduct = str(input("Введите название продукта: "))
            self.cost = float(input("Введите стоимость товара: "))
            self.date = input("Введите дату в формате DD/MM/YYYY: ")
        except ValueError:
            print("Ошибка ввода")
        return self

    def addDate(self, date_str):

        if date_str.rfind('/') != -1:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        else:
            print("Ошибка ввода даты.")
