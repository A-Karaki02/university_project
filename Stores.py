import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QComboBox,
                               QGraphicsDropShadowEffect, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)

import AddStore
import Basket
import EditProfile
import LoginPage
import Mainpage
import openAddBasketPage
import search
from DataBase import DataBase
from UserManager import user

# Firebase setup
db = DataBase.firebase.database()
numInBasket = 0


class Stores(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_items()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)  # Set the main layout of the widget
        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        self.layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", self.layout)
        self.layout.addSpacing(20)

        self.table_widget = QTableWidget()
        self.add_top_down_list([], self.table_widget)  # Initialize with empty data
        self.layout.addWidget(
            self.table_widget
        )  # Add the table widget to the main layout

        self.layout.addSpacing(10)

        # Create a new layout for the buttons
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        self.add_button("Add", 1, 1, grid_layout, self.openAddStorePage)
        if numInBasket == 0:
            self.add_button("Go To Basket", 0, 1, grid_layout, self.openBasket_Page)
        else:
            self.add_button(
                f"Go To Basket ({numInBasket})",
                0,
                1,
                grid_layout,
                self.openBasket_Page,
            )
        self.add_button("Back", 1, 0, grid_layout, self.openMain_Page)
        self.add_button("Search", 0, 0, grid_layout, self.search_page)

        self.setStyleSheet(
            "background-color: rgb(255, 255, 255);font-weight: bold;"
        )  # White background
        self.show()

    def add_dynamic_label(self, text, layout):
        layout_widget = QWidget(self)  # Create a widget to hold the layout
        layout_widget.setStyleSheet(
            "background-color: rgb(131, 170, 229);"
        )  # Set background color for the layout widget

        v_layout = QVBoxLayout(
            layout_widget
        )  # Use the layout widget as the parent for QVBoxLayout

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
        dropdown.addItems([user.get_username(), "Edit Profile", "Sign Out"])
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
        button.setStyleSheet(
            """
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
        )
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(135, 206, 250))
        shadow.setOffset(5, 5)
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

    def add_top_down_list(self, items, table_widget):
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
            row_count = table_widget.rowCount()
            table_widget.insertRow(row_count)

            table_widget.setItem(
                row_count, 0, QTableWidgetItem(item.get("storeName", ""))
            )
            table_widget.setItem(
                row_count, 1, QTableWidgetItem(item.get("itemName", ""))
            )
            table_widget.setItem(
                row_count, 2, QTableWidgetItem(item.get("itemType", ""))
            )
            table_widget.setItem(row_count, 3, QTableWidgetItem(item.get("price", "")))
            table_widget.setItem(
                row_count, 4, QTableWidgetItem(item.get("quantity", ""))
            )

            button = QPushButton("Add")
            button.setStyleSheet(
                """
                QPushButton {
                    background-color: rgb(131, 170, 229);
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: rgb(0,0,205);
                }
                """
            )
            button.clicked.connect(
                lambda checked=None, p_key=item["personKey"], i_key=item[
                    "itemNumber"
                ], s_name=item.get("storeName", ""), i_name=item.get(
                    "itemName", ""
                ), i_type=item.get(
                    "itemType", ""
                ), price=item.get(
                    "price", ""
                ), quantity=item.get(
                    "quantity", ""
                ): self.openAddBasketPage(
                    p_key, i_key, s_name, i_name, i_type, price, quantity
                )
            )
            table_widget.setCellWidget(
                row_count, len(headers) - 1, button
            )  # Add button to the last column

            # Set the background color of the row to white
            for col in range(len(headers)):
                if table_widget.item(row_count, col) is not None:
                    table_widget.item(row_count, col).setBackground(
                        QColor(235, 235, 235)
                    )

        # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black;font-size: 16px;")

    def load_items(self):
        items = self.fetch_data_from_firebase()
        if items:  # Check if items are fetched successfully
            self.add_top_down_list(items, self.table_widget)
        else:
            print("No items to display.")

    def fetch_data_from_firebase(self):
        try:
            data = db.child("items").get().val()
            print(
                f"Data fetched from Firebase: {data}"
            )  # Debug print to check the data structure

            if data is None:
                print("No data found in the Firebase database.")
                return []

            items = []

            # Check if the data is a list or a dictionary
            if isinstance(data, dict):
                for person_key, person_items in data.items():
                    if isinstance(person_items, dict):
                        for item_number, item_data in person_items.items():
                            item_data["personKey"] = person_key
                            item_data["itemNumber"] = item_number
                            items.append(item_data)
                    elif isinstance(person_items, list):
                        for index, item_data in enumerate(person_items):
                            item_data["personKey"] = person_key
                            item_data["itemNumber"] = index
                            items.append(item_data)
            elif isinstance(data, list):
                for index, person_items in enumerate(data):
                    if isinstance(person_items, dict):
                        for item_number, item_data in person_items.items():
                            item_data["personKey"] = index
                            item_data["itemNumber"] = item_number
                            items.append(item_data)
                    elif isinstance(person_items, list):
                        for item_index, item_data in enumerate(person_items):
                            item_data["personKey"] = index
                            item_data["itemNumber"] = item_index
                            items.append(item_data)
            else:
                print("Unexpected data structure from Firebase.")
                return []

            return items
        except Exception as e:
            print(f"Error fetching data from Firebase: {e}")
            return []

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

    def openAddBasketPage(
        self, person_key, item_key, storeName, itemName, itemType, price, quantity
    ):
        self.main = openAddBasketPage.add_basket(
            person_key, item_key, storeName, itemName, itemType, price, quantity
        )
        self.main.show()

        print(
            f"Add button clicked for item with person key: {person_key} and item key: {item_key}"
        )

    def openBasket_Page(self):
        self.Basket = Basket.Basket_page()
        self.Basket.show()
        self.close()

    def search_page(self):
        self.Search = search.search_page()
        self.Search.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Stores()
    mainWin.show()
    sys.exit(app.exec())
