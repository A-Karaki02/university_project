import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSpinBox, QVBoxLayout,
                               QWidget)

import Stores
from DataBase import DataBase as db
from UserManager import user


class search_page(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Search")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout(self)

        Item_name_label = QLabel("Item Name:")
        self.Item_name_edit = QLineEdit()
        layout.addWidget(Item_name_label)
        layout.addWidget(self.Item_name_edit)

        Item_type_label = QLabel("Item Type:")
        self.Item_type_combo = QComboBox()
        self.Item_type_combo.addItems(["Iron and Cement", "Electricals"])
        layout.addWidget(Item_type_label)
        layout.addWidget(self.Item_type_combo)

        self.label = QLabel("Price:", self)
        layout.addWidget(self.label)

        self.from_textbox = QLineEdit(self)
        self.from_textbox.setPlaceholderText("From :")
        layout.addWidget(self.from_textbox)

        self.To_textbox = QLineEdit(self)
        self.To_textbox.setPlaceholderText("To :")
        layout.addWidget(self.To_textbox)
        # Add validator to allow only integer input


        self.Quantity_label = QLabel("Quantity:")
        self.Quantity_edit = QLineEdit()
        layout.addWidget(self.Quantity_label)
        layout.addWidget(self.Quantity_edit)

        add_button = QPushButton("Add Item")
        add_button.clicked.connect(self.handle_add_item)
        layout.addWidget(add_button)

        self.show()

    def Search_store(self):
        if user.is_supplier():
            store_name = user.get_store_name()
        else:
            store_name = user.get_username()
        item_name = self.Item_name_edit.text()
        item_type = self.Item_type_combo.currentText()
        price = self.Price_edit.text()
        self.items = {"storeName": store_name, "itemName": item_name,"itemType": item_type, "price": price}

    def handle_add_item(self):
        self.add_store()

        user.add_item(self.items)
        self.close()
