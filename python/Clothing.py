from Product import Product

class Clothing(Product):
    def __init__(self):
        super().__init__()
        self.size = ""
        self.material = ""
        self.gender = ""

    def __init__(self, size="", material="", gender=""):
        super().__init__()
        self.size = size
        self.material = material
        self.gender = gender

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getMaterial(self):
        return self.material

    def setMaterial(self, material):
        self.material = material

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    # def display(self):
        # return super().display() + " {:<4s} | {:<8s} | {:<6s} |".format(self.size, self.material, self.gender)
