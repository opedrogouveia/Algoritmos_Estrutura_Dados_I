import sys
from PyQt5.QtWidgets import *
from abc import ABCMeta, abstractmethod

class Form(QMainWindow):
    def __init__(self, title="Vehicle Registration", width=400, height=200):
        super().__init__()
        self._title = title
        self.__width = width
        self.__height = height

        self.setWindowTitle(title)
        self.setGeometry(300, 300, width, height)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > self.__width:
            self.__width = value
        else:
            print("It's not allowed to add a width less than 300!")

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value > self.__height:
            self.__height = value
        else:
            print("It's not allowed to add a height less than 300!")

    def buildLayout(self):
        self.lblBranch = QLabel("Branch: ")
        self.txtBranch = QLineEdit(self)
        self.lblMileage = QLabel("Mileage: ")
        self.txtMileage = QLineEdit(self)
        self.layout.addWidget(self.lblBranch)
        self.layout.addWidget(self.txtBranch)
        self.layout.addWidget(self.lblMileage)
        self.layout.addWidget(self.txtMileage)
    
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def messageBox(self):
        pass