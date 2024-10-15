from ProductWindow import ProductWindow
from PyQt5.QtWidgets import QLineEdit, QLabel, QMessageBox
from Perishable import Perishable

class PerishableWindow(ProductWindow):
    def __init__(self, title = "Perishable Product Window"):
        super().__init__(title)

    def buildLayout(self):
        super().buildLayout()
        self.lblTemperature = QLabel("Max Temperature: ")
        self.txtTemperature = QLineEdit(self)
        self.layout.addWidget(self.lblTemperature)
        self.layout.addWidget(self.txtTemperature)
        self.setGeometry(300, 200, 300, 200)

    def save(self):
        perishable = Perishable(self.txtName.text())
        
        price = self.txtPrice.text()
        if len(price) > 0:
            price = price.replace(",", ".")
            perishable.price = float(price)
        
        temperature = self.txtTemperature.text()
        if len(temperature) > 0:
            temperature = temperature.replace(",", ".")
            perishable.maxTemperature = float(temperature)

        QMessageBox.information(self, "Saved Product!", str(perishable))

        # name = self.txtName.text()
        # price = self.txtPrice.text()
        # temp = self.txtTemp.text()
        # fPrice = 0.0
        # if price.__len__() > 0:
        #     price = price.replace(",", ".")
        #     fPrice = float(price)
        # txt = "Name: " + name + "\nPrice: " + str(fPrice) + "\nMax Temperature" + temp
        # QMessageBox.information(self, "Saved Product", txt)