# # from Vehicle import Vehicle
# # v = Vehicle("Jeep")

# from Car import Car

# c = Car()
# c.register()
# # c.km = 1000
# c.impress()

import sys
from PyQt5.QtWidgets import QApplication
from CarForm import CarForm
from MotorcycleForm import MotorcycleForm

app = QApplication(sys.argv)

car = CarForm()
car.show()

motorcycle = MotorcycleForm()
motorcycle.show()

sys.exit(app.exec_())