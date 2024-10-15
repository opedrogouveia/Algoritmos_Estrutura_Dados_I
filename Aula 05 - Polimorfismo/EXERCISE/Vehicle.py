class Vehicle():
    def __init__(self, brand, model, wheels, currentSpeed = 0):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.currentSpeed = currentSpeed
    
    def __str__(self):
        txt = f" Brand: {self.brand}"
        txt += f"\n Model: {self.model}"
        txt += f"\n Wheels Quantity: {self.wheels}"
        txt += f"\n Speed: {self.currentSpeed}km/h"
        return txt
    
    def accelerate(self, speed):
        self.currentSpeed = self.currentSpeed + speed

    def brake(self, brake):
        self.currentSpeed = self.currentSpeed - brake