import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,QGraphicsDropShadowEffect,
                               QWidget)

import checkout
import EditProfile
import LoginPage
import Mainpage
import SignupPage
from UserManager import user


class Basket_page(QWidget):
    def __init__(self):
        super().__init__()


        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)


        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        table_widget = QTableWidget()

        # Sample data
        items = [
            {"storeName": "Store A", "itemName": "Item 1", "itemType": "Type X", "price": 10, "quantity": 2},
            {"storeName": "Store B", "itemName": "Item 2", "itemType": "Type Y", "price": 20, "quantity": 3},
            {"storeName": "Store C", "itemName": "Item 3", "itemType": "Type Z", "price": 30, "quantity": 1}
        ]

        # Add the table to the layout
        self.add_top_down_list(items, table_widget, layout)

        # Set the layout
        self.setLayout(layout)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)
        self.add_button("Back", 0, 0, grid_layout, self.openMain_Page)
        self.add_button("Checkout", 0, 2, grid_layout, self.openCheckout_Page)



        self.setStyleSheet("background-color: rgb(255,255,255);font-weight: bold;")  # Black
        self.show()

    def add_dynamic_label(self, text, layout):
        layout_widget = QWidget(self)  # Create a widget to hold the layout
        layout_widget.setStyleSheet("background-color: rgb(131, 170, 229);")  # Set background color for the layout widget

        v_layout = QVBoxLayout(layout_widget)  # Use the layout widget as the parent for QVBoxLayout

        label = QLabel(text, self)
        label.setStyleSheet(
        "font-size: 32px;color: rgb(0, 0, 0);font-style: italic;font-weight: bold; background-color: rgb(131, 170, 229);"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(60)
        v_layout.addWidget(label)

        h_layout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(spacer)  # Add spacer to push the dropdown to the right

        dropdown = QComboBox(self)
        dropdown.addItems(
        [user.get_username(), "Edit Profile", "Sign Out"]
        )
        dropdown.setStyleSheet(
        "background-color: rgb(131, 170, 229); color: rgb(0, 0, 0);border: 2px solid black;"
        )
        dropdown.setFixedHeight(30)
        dropdown.setFixedWidth(120)
        h_layout.addWidget(dropdown)
        v_layout.addLayout(h_layout)

        layout.addWidget(layout_widget)  # Add the layout widget to the main layout

        dropdown.currentIndexChanged.connect(self.dropdown_changed)

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("""
                            QPushButton {
                            background-color: rgb(131, 170, 229);
                            font-weight: bold;
                            font-size: 16px;
                            border: 2px solid black;
                            border-radius: 30px;
                            }
                            QPushButton:hover {
                            background-color: rgb(0,0,205);
                            }
                            """
                            )  # White
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(135,206,250))
        shadow.setOffset(5,5)
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

    def add_top_down_list(self, items, table_widget, layout):
        headers = [
            "Store Name",
            "Item Name",
            "Item Type",
            "Price",
            "Quantity",
            "Total",
            "Remove",
        ]
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()
        header.setStyleSheet("background-color: rgb(131, 170, 229);")
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setVisible(False)  # Hide vertical header

        for item in items:
            # Add data rows
            table_widget.insertRow(table_widget.rowCount())

            table_widget.setItem(table_widget.rowCount() - 1, 0, QTableWidgetItem(item.get("storeName", "")))
            table_widget.setItem(table_widget.rowCount() - 1, 1, QTableWidgetItem(item.get("itemName", "")))
            table_widget.setItem(table_widget.rowCount() - 1, 2, QTableWidgetItem(item.get("itemType", "")))

            # Add columns with item data
            for col, header_text in enumerate(headers[3:]):
                item_value = item.get(header_text.lower(), "")
                table_item = QTableWidgetItem(str(item_value))
                table_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)  # Make cells non-editable
                table_item.setForeground(Qt.black)  # Set text color to black
                table_widget.setItem(table_widget.rowCount() - 1, col + 3, table_item)

            # Calculate total price dynamically and add it to the "Total" column
            price = float(item.get("price", 0))
            quantity = int(item.get("quantity", 0))
            total = price * quantity
            table_widget.setItem(table_widget.rowCount() - 1, 5, QTableWidgetItem(str(total)))

            # Add remove button to the "Remove" column
            button = QPushButton("Remove")
            button.setStyleSheet("""
                QPushButton {
                    background-color: rgb(255,0,0);
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: rgb(220,20,60);
                }
                """)
            button.clicked.connect(lambda _, row=table_widget.rowCount() - 1: self.remove_item(row, table_widget))
            table_widget.setCellWidget(table_widget.rowCount() - 1, 6, button)

            # Set the background color of the row to white
            for col in range(len(headers)):
                if table_widget.item(table_widget.rowCount() - 1, col) is not None:
                    table_widget.item(table_widget.rowCount() - 1, col).setBackground(QColor(235, 235, 235))

        # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black; font-size: 16px;")

        # Add the table to the layout
        layout.addWidget(table_widget)

    def remove_item(self, row, table_widget):
        table_widget.removeRow(row)

    def openMain_Page(self):
        self.main = Mainpage.MainPage()
        self.main.show()
        self.close()

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openEditProfile_Page(self):
        self.Edit = EditProfile.EditProfile()
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()

    def openCheckout_Page(self):
        self.Checkout = checkout.Checkout_page()
        self.Checkout.show()
