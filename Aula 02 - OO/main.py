from Person import Person
from City import City
from Category import Category
from Product import Product
from Order import Order

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

order01 = Order("Street A, 100")
order02 = Order("Street B, 200")

order02.addProduct(product01)
print(order02)
order02.addProduct(product02)
print(order02.addProduct(product04)) # RETURNS THE ORDER SUM
order02.printOrder()