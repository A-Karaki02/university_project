import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QLabel,
    QScrollArea,
    QHBoxLayout,
    QHeaderView,
    QTableWidgetItem,
    QTableWidget,
    QSizePolicy,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import AddStore
import EditProfile
import LoginPage
import Mainpage
import UserManager
import openAddBasketPage


class Stores(QWidget):
    def __init__(self, initial_size):
        super().__init__()
        self.resize(initial_size)
        self.initUI()
        self.table_widget = QTableWidget()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.table_widget = QTableWidget()
        self.setWindowTitle("GRADUATION PROJECT")
        # self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_logo_label("BuildSmart", layout)
        layout.addSpacing(20)

        table_layout = QVBoxLayout()
        layout.addLayout(table_layout)

        labels_layout = QHBoxLayout()
        table_layout.addLayout(labels_layout)

        self.add_top_down_list(
            [
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
                {
                    "itemName": "iron",
                    "storeName": "Jameed02",
                    "price": 200,
                    "quantity": 30,
                    "itemType": "iron and cement",
                },
            ],
            self.table_widget,
            table_layout,
        )
        layout.addSpacing(10)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.add_button("Add", 0, 5, grid_layout, self.openAddStorePage)

        self.add_button("Back", 100, 0, grid_layout, self.openMain_Page)
        self.add_button("Done", 100, 5, grid_layout, self.openMain_Page)

        self.add_button("test", 0, 0, grid_layout, self.search_page)

        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black
        self.show()

    def add_logo_label(self, text, layout):
        v_layout = QVBoxLayout()

        dropdown = QComboBox(self)
        dropdown.addItems(
            ["User Name", "Edit Profile", "Sign Out"]
        )  # Add your options here
        dropdown.setStyleSheet(
            "background-color: rgb(140, 140, 140); color: rgb(0, 0, 0);"
        )
        dropdown.setFixedHeight(30)
        dropdown.setFixedWidth(120)
        v_layout.addWidget(dropdown)
        v_layout.setAlignment(dropdown, Qt.AlignRight)  # Align dropdown to the right
        # v_layout.addStretch(1)
        layout.addLayout(v_layout)

        label = QLabel(text, self)
        label.setStyleSheet(
            "font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(100)
        v_layout.addWidget(label)

        dropdown.currentIndexChanged.connect(self.dropdown_changed)

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
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
            "Add To Basket",
        ]
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        for item in items:
            row_count = table_widget.rowCount()
            table_widget.insertRow(row_count)

            # Add "Store Name", "Item Name", and "Item Type" explicitly
            table_widget.setItem(
                row_count, 0, QTableWidgetItem(item.get("storeName", ""))
            )
            table_widget.setItem(
                row_count, 1, QTableWidgetItem(item.get("itemName", ""))
            )
            table_widget.setItem(
                row_count, 2, QTableWidgetItem(item.get("itemType", ""))
            )

            for col, header in enumerate(headers[3:], start=3):
                item_value = item.get(header.lower(), "")
                table_item = QTableWidgetItem(str(item_value))
                table_item.setFlags(
                    table_item.flags() ^ Qt.ItemIsEditable
                )  # Make cell non-editable
                table_widget.setItem(row_count, col, table_item)

            button = QPushButton("Add")
            button.setStyleSheet(
                "background-color: rgb(140, 140, 140); color: rgb(0, 0, 0);"
            )
            button.clicked.connect(self.openAddBasketPage)
            table_widget.setCellWidget(
                row_count, len(headers) - 1, button
            )  # Add button to the second last column

            # Set the background color of the row to white
            for col in range(len(headers)):
                table_widget.item(row_count, col).setBackground(Qt.white)

        # table_widget.setMaximumHeight(600)

        # Add the table to the layout
        layout.addWidget(table_widget)

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

    def openAddStorePage(self):
        self.add_store_page = AddStore.add_store()
        self.add_store_page.show()

    def openAddBasketPage(self):
        self.main = openAddBasketPage.add_basket()
        self.main.show()

    def search_page(self):
        pass
