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

        payment_method_label = QLabel("Payment Method:")
        self.payment_method_combo = QComboBox()
        self.payment_method_combo.addItems(["Choose", "Visa", "MasterCard", "Cash"])
        layout.addWidget(payment_method_label)
        layout.addWidget(self.payment_method_combo)

        saved_cards_label = QLabel("My Cards (Saved Cards):")
        self.saved_cards_combo = QComboBox()
        self.saved_cards_combo.addItems(
            ["**** **** **** 1432", "**** **** **** 3729", "**** **** **** 9284"]
        )
        layout.addWidget(saved_cards_label)
        layout.addWidget(self.saved_cards_combo)

        self.card_label = QLabel("Card No.:")
        layout.addWidget(self.card_label)

        self.card_textbox = QLineEdit(self)
        self.card_textbox.setPlaceholderText("Ex: 1234 5678 9101 2345")
        layout.addWidget(self.card_textbox)

        self.cvv_label = QLabel("CVV:")
        layout.addWidget(self.cvv_label)

        self.cvv_textbox = QLineEdit(self)
        self.cvv_textbox.setPlaceholderText("Ex: 123")
        layout.addWidget(self.cvv_textbox)

        self.validation_label = QLabel("Validation:")
        layout.addWidget(self.validation_label)

        self.validation_textbox = QLineEdit(self)
        self.validation_textbox.setPlaceholderText("Ex: 12/30")
        layout.addWidget(self.validation_textbox)

        self.set_textboxes_enabled(False)  # Initially disable the textboxes

        add_button = QPushButton("Buy")
        add_button.clicked.connect(self.handle_add_item)
        layout.addWidget(add_button)

        self.payment_method_combo.currentTextChanged.connect(
            self.handle_payment_method_change
        )
        self.show()

    def set_textboxes_enabled(self, enabled):
        self.card_textbox.setEnabled(enabled)
        self.cvv_textbox.setEnabled(enabled)
        self.validation_textbox.setEnabled(enabled)

    def handle_payment_method_change(self, text):
        if text in ["Visa", "MasterCard"]:
            self.set_textboxes_enabled(True)
        else:
            self.set_textboxes_enabled(False)

    def Checkout(self):
        if user.is_supplier():
            store_name = user.get_store_name()
        else:
            store_name = user.get_username()
        item_name = self.item_name_edit.text()
        item_type = self.payment_method_combo.currentText()
        price = self.price_edit.text()
        self.items = {
            "storeName": store_name,
            "itemName": item_name,
            "itemType": item_type,
            "price": price,
        }

    def handle_add_item(self):
        user.checkout_items()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Checkout_page()
    sys.exit(app.exec())
