from MotorizedVehicle import MotorizedVehicle

class Car(MotorizedVehicle):
    def __init__(self, brand, model, wheels, currentSpeed = 0, engineDisplacement = None, numDoors = 2):
        super().__init__(brand, model, wheels, currentSpeed, engineDisplacement)
        self.numDoors = numDoors

    def __str__(self):
        txt = super().__str__()
        txt += f"\n Doors Quantity: {self.numDoors}"
        txt += "\n---------------------------"
        return txt