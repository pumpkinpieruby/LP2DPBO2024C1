from Clothing import Clothing

class Shirt(Clothing):
    def __init__(self):
        super().__init__()
        self.color = ""
        self.sleeveType = ""

    def __init__(self, color="", sleeveType=""):
        super().__init__()
        self.color = color
        self.sleeveType = sleeveType

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getSleeveType(self):
        return self.sleeveType

    def setSleeveType(self, sleeveType):
        self.sleeveType = sleeveType

    # def display(self):
       # return super().display() + " {:<7s} | {:<6s} |".format(self.color, self.sleeveType)
