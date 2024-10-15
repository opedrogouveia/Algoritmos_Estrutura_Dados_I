from Bicycle import Bicycle
from Motorcycle import Motorcycle
from Car import Car

# class Bicycle
bike1 = Bicycle("Trek", "Marlin 7", 2, 25, 18, True)
bike2 = Bicycle("Giant", "Talon 2", 2, 28, 21, False)
bike3 = Bicycle("Specialized", "Rockhopper", 2, 30, 24, True)
bike4 = Bicycle("Cannondale", "Trail 5", 2, 26, 16, False)

# class Motorcycle
motorcycle1 = Motorcycle("Harley-Davidson", "Iron 883", 2, 120, "883cc", True)
motorcycle2 = Motorcycle("Yamaha", "MT-07", 2, 130, "689cc", True)
motorcycle3 = Motorcycle("Honda", "CB500F", 2, 140, "471cc", False)
motorcycle4 = Motorcycle("Kawasaki", "Ninja 400", 2, 150, "399cc", True)

# class Car
car1 = Car("Toyota", "Corolla", 4, 180, "1.8", 4)
car2 = Car("Ford", "Focus", 4, 190, "2.0", 4 )
car3 = Car("Honda", "Civic", 4, 200, "2.0", 4)
car4 = Car("Chevrolet", "Onix", 4, 175,  "1.0", 4)

print("* Bicycles: *\n")
print(bike1)
print(bike2)
print(bike3)
print(bike4)

print("\n* Motorcycles: *\n")
print(motorcycle1)
print(motorcycle2)
print(motorcycle3)
print(motorcycle4)

print("\n* Cars: *\n")
print(car1)
print(car2)
print(car3)
print(car4)