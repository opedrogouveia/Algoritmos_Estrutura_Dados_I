import sys
from PyQt5.QtWidgets import *
from Form import Form
from Car import Car

class CarForm(Form, QMainWindow):
    def __init__(self, title="Vehicle Registration", width=400, height=200):
        super().__init__(title, width, height)

        self.setWindowTitle(title)
        self.setGeometry(300, 300, width, height)
        self.layout = QVBoxLayout()
        self.buildLayout()

        self.saveButton = QPushButton("Save", self)
        self.saveButton.clicked.connect(self.save)
        self.layout.addWidget(self.saveButton)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def buildLayout(self):
        super().buildLayout()
        self.lblDoors = QLabel("Doors: ")
        self.txtDoors = QLineEdit(self)
        self.layout.addWidget(self.lblDoors)
        self.layout.addWidget(self.txtDoors)

    def save(self):
        if self.txtBranch and self.txtMileage and self.txtDoors:
            self.car = Car(self.txtBranch.text(), int(self.txtMileage.text()), int(self.txtDoors.text()))
            self.messageBox()
    
    def messageBox(self):
        QMessageBox.information(self, "Car Registered!", str(self.car))