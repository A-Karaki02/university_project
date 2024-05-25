import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSpinBox, QVBoxLayout,
                               QWidget)

import Stores
from DataBase import DataBase as db
from UserManager import user


class add_basket(QWidget):
    def __init__(self, Pk, Ik, Sn, In, It, p, q):
        super().__init__()
        self.person_key = Pk
        self.item_key = Ik
        self.storeName = Sn
        self.itemName = In
        self.itemType = It
        self.pricee = p
        self.quantity = q
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Add To Basket")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout(self)

        Item_name_label = QLabel("Item Name:")
        self.Item_name_edit = QLineEdit(self.itemName)
        layout.addWidget(Item_name_label)
        layout.addWidget(self.Item_name_edit)
        self.Item_name_edit.setReadOnly(True)

        Item_type_label = QLabel("Item Type:")
        self.Item_type_edit = QLineEdit(self.itemType)
        layout.addWidget(Item_type_label)
        layout.addWidget(self.Item_type_edit)
        self.Item_type_edit.setReadOnly(True)

        self.Price_label = QLabel("Price:")
        self.Price_edit = QLineEdit(self.pricee)
        layout.addWidget(self.Price_label)
        layout.addWidget(self.Price_edit)
        self.Price_edit.setReadOnly(True)

        self.Quantity_label = QLabel("Quantity:")
        self.Quantity_edit = QLineEdit()
        layout.addWidget(self.Quantity_label)
        layout.addWidget(self.Quantity_edit)

        add_button = QPushButton("Add Item")
        add_button.clicked.connect(self.handle_add_item)
        layout.addWidget(add_button)

        self.show()

    def add_store(self):
        store_name = self.storeName
        item_name = self.itemName
        item_type = self.itemType
        price = self.pricee
        quantity = self.Quantity_edit.text()
        oQuantity = self.quantity

        if store_name == user.get_username() or store_name == user.get_store_name():
            return False

        if int(quantity) > int(oQuantity):
            return False

        user.add_to_basket(
            self.person_key,
            self.item_key,
            store_name,
            item_name,
            item_type,
            price,
            quantity,
            oQuantity,
        )

        user.add_to_db_basket(self.person_key, self.item_key)
        Stores.numInBasket += 1

    def handle_add_item(self):
        self.add_store()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = add_basket()
    sys.exit(app.exec())
