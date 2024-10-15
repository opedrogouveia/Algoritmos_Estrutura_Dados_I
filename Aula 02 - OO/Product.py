from Category import Category

class Product:
    def __init__(self, name, price = 9.90, category = Category("Drinks")):
        self.id = None
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        txt = "----------------------------"
        txt += "\nName: " + self.name
        txt += "\nPrice: " + str(self.price)
        txt += "\nCategory: " + self.category.name
        return txt