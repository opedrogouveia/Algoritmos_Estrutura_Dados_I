import sys
from PyQt5.QtWidgets import QApplication
from ProductWindow import ProductWindow
from PerishableWindow import PerishableWindow

from City import City
from CityForm import CityForm

from Person import Person
from CustomerForm import CustomerForm

from CustomersList import CustomersList

cities = []
customers = []

app = QApplication(sys.argv)

ctyWindow = CityForm(cityArray = cities)
# cityWindow.show()

custWindow = CustomerForm(customersArray = customers, citiesArray = cities, cityWindow = ctyWindow)
# custWindow.show()

customersListWindow = CustomersList(customers, custWindow)
customersListWindow.show()

sys.exit(app.exec_())

# windowProduct = WindowProduct()
# windowProduct.show()

# windowPerishable = WindowPerishable()
# windowPerishable.show()