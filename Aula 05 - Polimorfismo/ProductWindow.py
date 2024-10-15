import sys
from PyQt5.QtWidgets import *
from Product import Product

class ProductWindow(QMainWindow):
    def __init__(self, title = "Product Window"):
        super().__init__()
        
        self.setWindowTitle(title)
        self.setGeometry(300, 200, 300, 200)
        self.layout = QVBoxLayout()
        self.buildLayout()
        
        self.btnSave = QPushButton("Save", self)
        self.btnSave.clicked.connect(self.save)
        self.layout.addWidget(self.btnSave)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def save(self):
        product = Product(None)
        product.name = self.txtName.text()
        price = self.txtPrice.text()
        product.price = 0.0
        if len(price) > 0:
            product.price = price.replace("," , ".")
        QMessageBox.information(self, "Saved Product!", str(product))

        # name = self.txtName.text()
        # price = self.txtPrice.text()
        # fPrice = 0.0
        # if price.__len__() > 0:
        #     price = price.replace(",", ".")
        #     fPrice = float(price)
        # txt = "Name: " + name + "\nPrice: " + str(fPrice)
        # QMessageBox.information(self, "Product Saved!", txt)
    
    def buildLayout(self):
        self.lblName = QLabel("Name: ")
        self.lblPrice = QLabel("Price: ")
        self.txtName = QLineEdit(self)
        self.txtPrice = QLineEdit(self)
        
        self.layout.addWidget(self.lblName)
        self.layout.addWidget(self.txtName)
        self.layout.addWidget(self.lblPrice)
        self.layout.addWidget(self.txtPrice)