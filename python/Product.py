class Product:
    def __init__(self):
        self.idProduct = ""
        self.name = ""
        self.brand = ""
        self.price = ""

    def __init__(self, id="", name="", brand="", price=""):
        self.idProduct = id
        self.name = name
        self.brand = brand
        self.price = price

    def getIdProduct(self):
        return self.idProduct

    def setIdProduct(self, idProduct):
        self.idProduct = idProduct

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    # def display(self):
       #  return "| {:<9d} | {:<15s} | {:<11s} | ${:<7.2f} |".format(self.idProduct, self.name, self.brand, self.price)
