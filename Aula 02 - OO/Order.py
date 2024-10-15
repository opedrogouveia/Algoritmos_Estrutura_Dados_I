from Person import Person
from Product import Product

class Order:
    def __init__(self, address, customer = None):
        self.id = None
        self.address = address
        self.customer = customer
        self.__products = []
        
    def addProduct(self, prod):
        if prod is not None:
            self.__products.append(prod)
        sum = 0
        for p in self.__products:
            sum += p.price
        return sum
    
    def __str__(self):
        txt = "Address: " + self.address
        txt += "\nCustomer: " + str(self.customer)
        txt += "\nProducts: \n"
        for p in self.__products:
            txt += str(p) + "\n"
        return txt
    
    def printOrder(self):
        print(self)
      # print(self.__str__())