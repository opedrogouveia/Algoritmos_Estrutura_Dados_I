from Vehicle import Vehicle

class MotorizedVehicle(Vehicle):
    def __init__(self, brand, model, wheels, currentSpeed = 0, engineDisplacement = None):
        super().__init__(brand, model, wheels, currentSpeed)
        self.engineDisplacement = engineDisplacement

    def __str__(self):
        txt = super().__str__()
        txt += f"\n Engine Displacement: {self.engineDisplacement}"
        return txt