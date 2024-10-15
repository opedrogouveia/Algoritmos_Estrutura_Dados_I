import sys
from PyQt5.QtWidgets import *
from City import City
from Person import Person
# from CityForm import CityForm

class CustomerForm(QMainWindow):

    def __init__(self, title = "Customer Registration", customersArray = [], citiesArray = [], cityWindow = None) :
        super().__init__()
        self.customers = customersArray
        self.cities = citiesArray
        self.cityWindow = cityWindow
        self.customersListWindow = None

        if self.cityWindow is not None:
            self.cityWindow.customerWindow = self

        self.setWindowTitle(title)
        self.setGeometry(750, 300, 500, 150)
        self.layout = QVBoxLayout()
        self.buildLayout()

        self.saveButton = QPushButton("Save", self)
        self.saveButton.clicked.connect(self.__save)
        self.layout.addWidget(self.saveButton)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def buildLayout(self):
        self.lblName = QLabel("Name: ")
        self.txtName = QLineEdit(self)
        self.layout.addWidget( self.lblName)
        self.layout.addWidget( self.txtName)

        self.lblHeight = QLabel("Height: ")
        self.txtHeight = QLineEdit(self)
        self.layout.addWidget( self.lblHeight)
        self.layout.addWidget( self.txtHeight)

        # self.loadCitiesButton = QPushButton("Atualiza Lista de Cidades", self)
        # self.loadCitiesButton.clicked.connect(self.loadCities)
        # self.layout.addWidget(self.loadCitiesButton)

        self.lblCity = QLabel("City: ")
        self.cmbCity = QComboBox(self)
        self.cmbCity.currentIndexChanged.connect(self.__openCityWindow)
        self.layout.addWidget(self.lblCity)
        self.layout.addWidget(self.cmbCity)
        self.loadCities()

    def __openCityWindow(self):
        if self.cmbCity.currentIndex() == 1:
            self.cityWindow.show()

    def loadCities(self):
        self.cmbCity.clear()
        self.cmbCity.addItem("Select...", None)
        self.cmbCity.addItem("Add new city...", None)
        for cty in self.cities:
            self.cmbCity.addItem(cty.name, cty)

    def __save(self):
        if len(self.txtName.text()) > 0:
            cust = Person(self.txtName.text())
            height = self.txtHeight.text()
            if len(height) > 0:
                height = height.replace(",", ".")
                cust.height = float(height)
            if self.cmbCity.currentIndex() > 0:
                cust.city = self.cmbCity.currentData()
            self.customers.append(cust)

            self.txtName.clear()
            self.txtHeight.clear()
            self.cmbCity.setCurrentIndex(0)
            QMessageBox.information(self, "Saved Customer!" , str(cust) )
            self.customersListWindow.updateTable()
            self.hide()