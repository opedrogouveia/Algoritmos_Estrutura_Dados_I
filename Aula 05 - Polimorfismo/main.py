from Person import Person
from City import City
from Category import Category
from Product import Product
from Order import Order
from Perishable import Perishable

city1 = City()
city2 = City("Porto Alegre")

p1 = Person("João")
p2 = Person("Maria", 1.80)
p3 = Person("José", 1.80, city1)
p4 = Person("Julia", city2)
p5 = Person("Suzy", city = city2)

category01 = Category()
category02 = Category("Foods")

product01 = Product("Coca-Cola")
product02 = Product("Fanta", 7.90)
product03 = Product("1L Jar", 19.90, category01)
product04 = Product("Rice", category = category01)

perProduct01 = Perishable("Alface", maxTemperature = 10)
perProduct01 = Perishable("Iogurte", 6.90, maxTemperature = 5)
perProduct01 = Perishable("Queijo", 36.90, category01)
perProduct01 = Perishable("Sorvete", 19.90, category02, -18)

order01 = Order("Street A, 100")
order02 = Order("Street B, 200")

order02.addProduct(product01)
print(order02)
order02.addProduct(product02)
print(order02.addProduct(product04)) # RETURNS THE ORDER SUM
order02.printOrder()