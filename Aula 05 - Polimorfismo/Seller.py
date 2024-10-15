from City import City
from Person import Person

class Seller(Person):
    def __init__(self, name, height=1.73, city = City("Porto Alegre"), wage = 1200):
          super().__init__(name, height, city)
          self.wage = wage
          
    def register(self):
        self = super().register()
        self.wage = float(input("Digite o salário: "))
        return self