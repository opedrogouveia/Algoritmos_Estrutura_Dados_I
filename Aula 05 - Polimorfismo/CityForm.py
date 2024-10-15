import sys
from PyQt5.QtWidgets import *
from City import City
from CustomerForm import CustomerForm

class CityForm(QMainWindow):
    def __init__(self, title="City Registration", cityArray = [], customerWindow = None) :
        super().__init__()
        self.cities = cityArray
        self.customerWindow = customerWindow

        self.setWindowTitle(title)
        self.setGeometry(300, 300, 400, 150)    
        self.layout = QVBoxLayout()
        self.buildLayout()

        self.saveButton = QPushButton("Save", self)
        self.saveButton.clicked.connect(self.save)
        self.layout.addWidget(self.saveButton)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def buildLayout(self):
        self.lblName = QLabel("Name: ")
        self.txtName = QLineEdit(self)
        self.layout.addWidget(self.lblName)
        self.layout.addWidget(self.txtName)

    def save(self):
        if len(self.txtName.text()) > 0:
            cty = City(self.txtName.text())
            self.cities.append(cty)
            self.txtName.clear()
            QMessageBox.information(self, "Saved City!", str(cty))
            self.customerWindow.loadCities()
            self.hide()