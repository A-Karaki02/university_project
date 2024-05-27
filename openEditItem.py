# import sys

# from PySide6.QtCore import QSize, Qt
# from PySide6.QtWidgets import (
#     QApplication,
#     QComboBox,
#     QGridLayout,
#     QLabel,
#     QLineEdit,
#     QMessageBox,
#     QPushButton,
#     QSpinBox,
#     QVBoxLayout,
#     QWidget,
# )

# import Stores
# from DataBase import DataBase as db
# from UserManager import user


# class edit_item(QWidget):
#     def __init__(self, item_key):
#         super().__init__()
#         self.itemKey = item_key
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Edit item")
#         self.setFixedSize(400, 250)

#         layout = QVBoxLayout(self)

#         self.Price_label = QLabel("Price:")
#         self.Price_edit = QLineEdit()
#         layout.addWidget(self.Price_label)
#         layout.addWidget(self.Price_edit)

#         self.Quantity_label = QLabel("Quantity:")
#         self.Quantity_edit = QLineEdit()
#         layout.addWidget(self.Quantity_label)
#         layout.addWidget(self.Quantity_edit)

#         add_button = QPushButton("Edit Item")
#         add_button.clicked.connect(self.edit_item())
#         layout.addWidget(add_button)

#         self.show()

#     def edit_item(self):
#         print("edit item is called")
#         price = self.Price_edit.text()
#         quantity = self.Quantity_edit.text()

#         user.edit_item(
#             self.itemKey,
#             price,
#             quantity,
#         )

#         self.close()
#         return True

#     def handle_add_item(self):
#         if self.edit_item:
#             self.close()

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QMessageBox, QPushButton, QSpinBox,
                               QVBoxLayout, QWidget)

import Stores
from DataBase import DataBase as db
from UserManager import user


class edit_item(QWidget):
    def __init__(self, item_key):
        super().__init__()
        self.itemKey = item_key
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Edit item")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout(self)

        self.Price_label = QLabel("Price:")
        self.Price_edit = QLineEdit()
        layout.addWidget(self.Price_label)
        layout.addWidget(self.Price_edit)

        self.Quantity_label = QLabel("Quantity:")
        self.Quantity_edit = QLineEdit()
        layout.addWidget(self.Quantity_label)
        layout.addWidget(self.Quantity_edit)

        add_button = QPushButton("Edit Item")
        add_button.clicked.connect(
            self.edit_item
        )  # Pass function reference without calling it
        layout.addWidget(add_button)

        self.show()

    def edit_item(self):
        print("edit item is called")
        price = self.Price_edit.text()
        quantity = self.Quantity_edit.text()

        user.edit_item(
            self.itemKey,
            quantity,
            price,
        )

        self.close()
        return True

    def handle_add_item(self):
        if self.edit_item:
            self.close()


# Assuming the following lines are used to test the edit_item widget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    item_key = (
        "example_key"  # Replace with the actual key for the item you want to edit
    )
    window = edit_item(item_key)
    sys.exit(app.exec())
