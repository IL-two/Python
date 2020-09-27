from Script.Product import Product


# Создание листа объектов
class ProductList(list):
    def __init__(self):
        self.__listProduct = list()

    def addProduct(self, product):
        self.__listProduct.append(product)
        # product = Product()
        # self.__listProduct.append(product.addProduct())

    def addProd(self):
        product = Product()
        self.__listProduct.append(product.addProduct())

    def display(self):
        print("{:<15}{:<15}{:<15}{}".format("Категория:", "Имя:", "Стоимость:", "Дата:"))
        for item in self.__listProduct:
            print("{0:<15}{1:<15}{2:<15}{3}".format(item.nameCategory,
                                                    item.nameProduct,
                                                    item.cost,
                                                    item.date))

    def getCategory(self, categoryName):
        print("{:<15}{:<15}{:<15}{}".format("Категория:", "Имя:", "Стоимость:", "Дата:"))
        i = 0
        for item in self.__listProduct:
            if item.nameCategory == categoryName:
                print("{0:<15}{1:<15}{2:<15}{3}".format(item.nameCategory,
                                                        item.nameProduct,
                                                        item.cost,
                                                        item.date))
                i = i + 1
        if i == 0:
            print("Такая категория не найдена")
