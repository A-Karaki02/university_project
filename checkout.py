import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QSpinBox, QVBoxLayout,
                               QWidget)

import Stores
from DataBase import DataBase as db
from UserManager import user


class Checkout_page(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Checkout")
        self.setFixedSize(450, 300)

        layout = QVBoxLayout(self)

        Item_type_label = QLabel("Payment Method:")
        self.Item_type_combo = QComboBox()
        self.Item_type_combo.addItems(["Choose", "Visa", "MasterCard", "Cash"])
        layout.addWidget(Item_type_label)
        layout.addWidget(self.Item_type_combo)

        Item_type_label = QLabel("My Cards (Saved Cards):")
        self.Item_type_combo = QComboBox()
        self.Item_type_combo.addItems(
            ["**** **** **** 1432", "**** **** **** 3729", "**** **** **** 9284"]
        )
        layout.addWidget(Item_type_label)
        layout.addWidget(self.Item_type_combo)

        self.Card_label = QLabel("Card No.:")
        layout.addWidget(self.Card_label)

        self.Card_textbox = QLineEdit(self)
        self.Card_textbox.setPlaceholderText("Ex : 1234 5678 9101 2345")
        layout.addWidget(self.Card_textbox)

        self.CVV_label = QLabel("CVV :")
        layout.addWidget(self.CVV_label)

        self.CVV_textbox = QLineEdit(self)
        self.CVV_textbox.setPlaceholderText("Ex : 123")
        layout.addWidget(self.CVV_textbox)

        self.Validation_label = QLabel("Validation :")
        layout.addWidget(self.Validation_label)

        self.Validation_textbox = QLineEdit(self)
        self.Validation_textbox.setPlaceholderText("Ex : 12/30")
        layout.addWidget(self.Validation_textbox)

        add_button = QPushButton("Buy")
        add_button.clicked.connect(self.handle_add_item)
        layout.addWidget(add_button)

        self.Item_type_combo.currentTextChanged.connect(
            self.handle_payment_method_change
        )
        self.show()

    def handle_payment_method_change(self, text):
        # Enable textboxes if Visa or MasterCard is selected
        if text in ["Visa", "MasterCard"]:
            self.Card_textbox.setEnabled(True)
            self.CVV_textbox.setEnabled(True)
            self.Validation_textbox.setEnabled(True)
        else:
            # Disable textboxes otherwise
            self.Card_textbox.setEnabled(False)
            self.CVV_textbox.setEnabled(False)
            self.Validation_textbox.setEnabled(False)

    def Checkout(self):
        if user.is_supplier():
            store_name = user.get_store_name()
        else:
            store_name = user.get_username()
        item_name = self.Item_name_edit.text()
        item_type = self.Item_type_combo.currentText()
        price = self.Price_edit.text()
        self.items = {
            "storeName": store_name,
            "itemName": item_name,
            "itemType": item_type,
            "price": price,
        }

    def handle_add_item(self):
        self.add_store()

        user.add_item(self.items)
        self.close()
