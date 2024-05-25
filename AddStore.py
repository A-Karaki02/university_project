import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSpinBox, QVBoxLayout,
                               QWidget)

import Stores
from DataBase import DataBase as db
from UserManager import user


class add_store(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add a new Store")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout(self)

        Item_name_label = QLabel("Item Name:")
        self.Item_name_edit = QLineEdit()
        layout.addWidget(Item_name_label)
        layout.addWidget(self.Item_name_edit)

        Item_type_label = QLabel("Item Type:")
        self.Item_type_combo = QComboBox()
        self.Item_type_combo.addItems(
            ["Construction Materiales", "Electricals", "Mechanices"]
        )
        layout.addWidget(Item_type_label)
        layout.addWidget(self.Item_type_combo)

        self.Price_label = QLabel("Price/Kg:")
        self.Price_edit = QLineEdit()
        layout.addWidget(self.Price_label)
        layout.addWidget(self.Price_edit)

        self.Quantity_label = QLabel("Quantity:")
        self.Quantity_edit = QLineEdit()
        layout.addWidget(self.Quantity_label)
        layout.addWidget(self.Quantity_edit)

        add_button = QPushButton("Add Item")
        add_button.clicked.connect(self.handle_add_item)
        layout.addWidget(add_button)

        self.show()

    def add_store(self):
        if user.is_supplier():
            store_name = user.get_store_name()
        else:
            store_name = user.get_username()
        item_name = self.Item_name_edit.text()
        item_type = self.Item_type_combo.currentText()
        price = self.Price_edit.text()
        quantity = self.Quantity_edit.text()
        self.items = {
            "storeName": store_name,
            "itemName": item_name,
            "itemType": item_type,
            "price": price,
            "quantity": quantity,
        }

    def handle_add_item(self):
        self.add_store()

        user.add_item(self.items)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = add_store()
    sys.exit(app.exec())
