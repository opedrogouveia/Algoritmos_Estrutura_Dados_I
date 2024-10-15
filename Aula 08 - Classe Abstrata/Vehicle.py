from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, branch, mileage=0):
        self.id = None
        self._branch = branch
        self.__mileage = mileage

    @property
    def mileage(self):
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value):
        if value > self.__mileage:
            self.__mileage = value
        else:
            print("Values not allowed!")

    @abstractmethod
    def register(self):
        pass
    
    def __str__(self):
        txt = "Branch: " + self._branch
        txt += "\nMileage: " + str(self.__mileage) + "Km"
        return txt
    
    def impress(self):
        print(self)