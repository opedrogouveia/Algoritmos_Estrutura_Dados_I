from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, branch=None, mileage=0, engineDisplacement = 50):
        super().__init__(branch, mileage)
        self.engineDisplacement = engineDisplacement

    def register(self):
        self._branch = input("Type the Branch Motorcycle: ")
        self.km = int(input("Type the Km Motorcycle: "))
        self.numDoors = int(input("Engine Displacement(cc): "))
        
    def __str__(self):
        txt = "\nEngine Displacement: " + str(self.engineDisplacement) + "cc"
        return super().__str__() + txt