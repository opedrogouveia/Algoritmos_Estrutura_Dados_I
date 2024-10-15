from Product import Product
from City import City
from Person import Person

class Customer(Person):
    def __init__(self, name, height=1.73, city = City("Canoas"), limit = 500):
        super().__init__(name, height, city)
        self.limit = limit

    def __str__(self):
        txt = super().__str__()
        txt += "\nLimit: $ " + str(self.limit)
        return txt
        
    def register(self):
        self = super().register()
        self.limit = float(input("Digite o limite: "))
        return self