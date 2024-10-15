from City import City

class Person:
    def __init__(self, name, height = 1.73, city = City("Itati")):
        self.id = None
        self.name = name
        self.height = height
        self.city = city
        
    def __str__(self):
        txt = "Name: " + self.name
        txt += "\nHeight: " + str(self.height)
        txt += "\nCity: " + self.city.name
        return txt