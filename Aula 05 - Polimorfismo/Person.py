from City import City

class Person:
    def __init__(self, name, height = 1.73, city = City("Itati")):
        self.id = None
        self.__name = name
        self.__height = height
        self.city = city

    # MÉTODO ACESSOR | -- GETTER --
    def getName(self):
        return self.__name
    
    # METODO MODIFICADOR | -- SETTER --
    def setName(self, value):
        if value > 0:
            self.__name = value
        else:
            print("Invalid Values for the 'Name'.")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value
        else:
            print("Invalid Values for the 'Name'.")

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print("Invalid Values for the 'Height'.")
    
    def __str__(self):
        txt = "Name: " + self.name
        txt += "\nHeight: " + str(self.height)
        txt += "\nCity: " + self.city.name
        return txt
    
    def register(self):
        self.name = input("Type the name's person: ")
        self.height = float(input("Type the height: "))
        self.city = City(input("Type the city: "))
        return self