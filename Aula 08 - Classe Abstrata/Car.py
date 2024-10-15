from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, branch=None, mileage=0, doors=4):
        super().__init__(branch, mileage)
        self.numDoors = doors

    def register(self):
        self._branch = input("Type the Branch Car: ")
        self.km = int(input("Type the Km Car: "))
        self.numDoors = int(input("Quantity doors: "))
        
    def __str__(self):
        txt = "\nDoors: " + str(self.numDoors)
        return super().__str__() + txt