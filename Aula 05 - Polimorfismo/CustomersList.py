from PyQt5.QtWidgets import *
from Customer import Customer

class CustomersList(QMainWindow):

    def __init__(self, customersList = [] , customerWindow = None ) :
        super().__init__()
        self.customers = customersList
        self.customerWindow = customerWindow
        if self.customerWindow is not None:
            self.customerWindow.customersListWindow = self

        self.setWindowTitle("Registered Customers")
        self.setGeometry(200, 200, 600, 300)
        self.layout = QVBoxLayout()

        self.openFormButton = QPushButton("Add Customer", self)
        self.openFormButton.clicked.connect(self.openForm)
        self.layout.addWidget(self.openFormButton)

        self.table = QListWidget(self)
        for cust in self.customers:
            self.table.addItem(str(cust), cust)
        self.layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def openForm(self):
        self.customerWindow.show()

    def updateTable(self):
        self.table.clear()
        for cust in self.customers:
            self.table.addItem(str(cust))