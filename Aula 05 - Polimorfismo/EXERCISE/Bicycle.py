from Vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, brand, model, wheels = 2, currentSpeed = 0, numGears = None, rearRack = False):
        super().__init__(brand, model, wheels, currentSpeed)
        self.numGears = numGears
        self.rearRack = rearRack

    def __str__(self):
        txt = super().__str__()
        txt += f"\n Gear Quantity: {self.numGears}"
        txt += f"\n Rear Rack: {self.rearRack}"
        txt += "\n---------------------------"
        return txt