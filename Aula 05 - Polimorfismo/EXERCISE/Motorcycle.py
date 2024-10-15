from MotorizedVehicle import MotorizedVehicle

class Motorcycle(MotorizedVehicle):
    def __init__(self, brand, model, wheels, currentSpeed = 0, engineDisplacement = None, electricStart = False):
        super().__init__(brand, model, wheels, currentSpeed, engineDisplacement)
        self.electricStart = electricStart

    def __str__(self):
        txt = super().__str__()
        txt += f"\n Electric Start: {self.electricStart}"
        txt += "\n---------------------------"
        return txt