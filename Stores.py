import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor
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
    QSpacerItem,

    
)

import AddStore
import Basket
import EditProfile
import LoginPage
import Mainpage
import UserManager
import openAddBasketPage
import search
from UserManager import user


class Stores(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        

    def initUI(self):
        layout = QVBoxLayout(self)
        self.table_widget = QTableWidget()
        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
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

        self.add_button("Add", 1, 1, grid_layout, self.openAddStorePage)
        self.add_button("Go To Basket", 0, 1, grid_layout, self.openBasket_Page)
        self.add_button("Back", 1, 0, grid_layout, self.openMain_Page)

        self.add_button("Search", 0, 0, grid_layout, self.search_page)

        self.setStyleSheet("background-color: rgb(255, 255, 255);font-weight: bold;")  # Black
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
        button.setStyleSheet("background-color: rgb(131, 170, 229);")  # White
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

    from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton

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
        header.setStyleSheet("background-color: rgb(131, 170, 229);")
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setVisible(False)  # Hide vertical header

        
        for item in items:
        # Add data rows
            table_widget.insertRow(table_widget.rowCount())

        # Add "Store Name", "Item Name", and "Item Type" explicitly
            table_widget.setItem(
            table_widget.rowCount() - 1, 0, QTableWidgetItem(item.get("storeName", ""))
            )
            table_widget.setItem(
            table_widget.rowCount() - 1, 1, QTableWidgetItem(item.get("itemName", ""))
            )
            table_widget.setItem(
            table_widget.rowCount() - 1, 2, QTableWidgetItem(item.get("itemType", ""))
            )

            for col, header_text in enumerate(headers[3:], start=3):
                item_value = item.get(header_text.lower(), "")
                table_item = QTableWidgetItem(str(item_value))
                table_item.setFlags(
                table_item.flags() ^ Qt.ItemIsEditable
                )  # Make cell non-editable
                table_widget.setItem(table_widget.rowCount() - 1, col, table_item)
                table_item.setForeground(Qt.black)  # Set text color to black for all columns

            button = QPushButton("Add")
            button.setStyleSheet(
            "background-color: rgb(131, 170,229);font-weight: bold;;"
            )
            button.clicked.connect(self.openAddBasketPage)
            table_widget.setCellWidget(
            table_widget.rowCount() - 1, len(headers) - 1, button
            )  # Add button to the second last column

        # Set the background color of the row to white
            for col in range(len(headers)):
                if table_widget.item(table_widget.rowCount() - 1, col) is not None:
                    table_widget.item(table_widget.rowCount() - 1, col).setBackground(QColor(235, 235, 235))
        
    # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black;")

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

    def openBasket_Page(self):
        self.Basket = Basket.Basket_page()
        self.Basket.show()
        self.close()

    def search_page(self):
        self.Search = search.serach_page()
        self.Basket.show()
        self.close()
