from Seller import Seller
from Customer import Customer
from Person import Person
from Perishable import Perishable

# prodPer = Perishable(None)

# print(prodPer.register())

customer01 = Customer("Pedro")
customer01.register()
print(customer01)

seller01 = Seller("João")
seller01.register()
print(seller01)