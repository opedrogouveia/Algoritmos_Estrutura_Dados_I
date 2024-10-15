from Category import Category
from Product import Product

class Perishable(Product):
    def __init__(self, nameP, priceP = 1.5, categoryP = Category("Frozen"), maxTemperature = 7):
        super().__init__(nameP, priceP, categoryP)
        self.maxTemperature = maxTemperature
        
    def __str__(self):
        txt = super().__str__()
        txt += "\nMaximun Temperature: " + str(self.maxTemperature)
        return txt
    
    def register(self):
        self = super().register()
        self.maxTemperature = float(input("Digite a temperatura máxima: "))
        return self