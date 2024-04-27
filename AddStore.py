import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QVBoxLayout, QWidget)

import Stores


class add_store(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add a new Store")
        self.setFixedSize(400, 150)

        layout = QVBoxLayout(self)

        store_name_label = QLabel("Store Name:")
        self.store_name_edit = QLineEdit()
        layout.addWidget(store_name_label)
        layout.addWidget(self.store_name_edit)

        store_type_label = QLabel("Store Type:")
        self.store_type_combo = QComboBox()
        self.store_type_combo.addItems(["Iron and Cement", "Electricals"])
        layout.addWidget(store_type_label)
        layout.addWidget(self.store_type_combo)

        add_button = QPushButton("Add Store")
        add_button.clicked.connect(self.add_store)
        layout.addWidget(add_button)

        self.show()

    def add_store(self):
        store_name = self.store_name_edit.text()
        store_type = self.store_type_combo.currentText()
        self.store_added.emit(store_name, store_type)
        self.close()
