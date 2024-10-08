import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (QApplication, QComboBox,
                               QGraphicsDropShadowEffect, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)

import AddStore
import Basket
import EditProfile
import LoginPage
import Mainpage
import openAddBasketPage
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
        self.setWindowTitle("BuildSmart")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(0, 0, 1200, 600)

        self.layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", self.layout)
        self.layout.addSpacing(20)

        # Search input field
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search...")

        search_button = QPushButton("Search", self)
        search_button.clicked.connect(self.search_items)
        search_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgb(10,22,39);
                font-weight: bold;
                font-size: 16px;
                color: rgb(255,255,255);
                border: 2px solid black;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: rgb(0,0,205);
            }
            """
        )
        search_button.setFixedWidth(150)

        delete_button = QPushButton("Delete Search", self)
        delete_button.clicked.connect(self.delete_search)
        delete_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgb(10,22,39);
                font-weight: bold;
                font-size: 16px;
                color: rgb(255,255,255);
                border: 2px solid black;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: rgb(0,0,205);
            }
            """
        )
        delete_button.setFixedWidth(150)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        search_layout.addWidget(delete_button)
        self.layout.addLayout(search_layout)

        self.table_widget = QTableWidget()
        self.add_top_down_list([], self.table_widget)  # Initialize with empty data
        self.layout.addWidget(
            self.table_widget
        )  # Add the table widget to the main layout

        self.layout.addSpacing(10)

        # Create a new layout for the buttons
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        self.add_button("Add Item", 0, 1, grid_layout, self.openAddStorePage)
        if numInBasket == 0:
            self.add_button("Go To Basket", 0, 2, grid_layout, self.openBasket_Page)
        else:
            self.add_button(
                f"Go To Basket ({numInBasket})", 0, 2, grid_layout, self.openBasket_Page
            )
        self.add_button("Back", 0, 0, grid_layout, self.openMain_Page)
        # self.add_button("Search", 0, 0, grid_layout, self.search_items)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")  # White background
        self.show()

    def add_dynamic_label(self, text, layout):
        layout_widget = QWidget(self)  # Create a widget to hold the layout
        layout_widget.setStyleSheet(
            "background-color: rgb(10,22,39);"
        )  # Set background color for the layout widget

        v_layout = QVBoxLayout(
            layout_widget
        )  # Use the layout widget as the parent for QVBoxLayout

        label = QLabel(text, self)
        label.setText(
            '<span style="font-size: 46px; color: rgb(255, 0, 0); font-style: italic;">Build</span>'
            '<span style="font-size: 46px; color: rgb(255, 255, 255); font-style: italic;">Smart</span>'
        )
        label.setStyleSheet("background-color: rgb(10,22,39);")
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(60)
        v_layout.addWidget(label)

        h_layout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(spacer)  # Add spacer to push the dropdown to the right

        dropdown = QComboBox(self)
        dropdown.addItems([user.get_username(), "Edit Profile", "Sign Out"])
        dropdown.setStyleSheet(
            "background-color: rgb(10,22,39); color: rgb(255, 255, 255);border: 0px solid black;"
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
                background-color: rgb(10,22,39);
                font-weight: bold;
                font-size: 16px;
                color: rgb(255,255,255);
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
            "Item Name",
            "Store Name",
            "Item Type",
            "Price/Kg",
            "Quantity",
            "Add To Basket",
        ]
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()
        header.setStyleSheet("background-color: rgb(10,22,39);")
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setVisible(False)  # Hide vertical header

        items = sorted(items, key=lambda x: x.get("itemName", "").lower())

        last_item_name = None

        for item in items:
            # Add data rows
            row_count = table_widget.rowCount()
            table_widget.insertRow(row_count)

            item_name = item.get("itemName", "")

            if item_name == last_item_name:
                table_widget.setItem(row_count, 0, QTableWidgetItem(""))  # Blank cell
            else:
                table_widget.setItem(row_count, 0, QTableWidgetItem(item_name))
                last_item_name = item_name

            table_widget.setItem(
                row_count, 1, QTableWidgetItem(item.get("storeName", ""))
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
                    background-color: rgb(10,22,39);
                    color: rgb(255, 255, 255);
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
            for col in range(len(headers)):
                item = table_widget.item(row_count, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

            # Set the background color of the row to white
            for col in range(len(headers)):
                if table_widget.item(row_count, col) is not None:
                    table_widget.item(row_count, col).setBackground(
                        QColor(235, 235, 235)
                    )

        # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black;font-size: 16px;")

    def load_items(self):
        self.items = self.fetch_data_from_firebase()
        if self.items:  # Check if items are fetched successfully
            self.add_top_down_list(self.items, self.table_widget)
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
                            if item_data is not None:  # Filter out None values
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
                            if item_data is not None:  # Filter out None values
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
        self.main.setGeometry(self.geometry())  # Set geometry to match current window
        self.main.show()
        self.close()

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openEditProfile_Page(self):
        self.Edit = EditProfile.EditProfile()
        self.Edit.setGeometry(self.geometry())  # Set geometry to match current window
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

    def search_items(self):
        query = self.search_input.text().lower()
        filtered_items = [
            item
            for item in self.items
            if query in item.get("storeName", "").lower()
            or query in item.get("itemName", "").lower()
            or query in item.get("itemType", "").lower()
        ]
        self.table_widget.setRowCount(0)  # Clear the table
        self.add_top_down_list(filtered_items, self.table_widget)

    def delete_search(self):
        self.search_input.clear()
        self.table_widget.setRowCount(0)  # Clear the table
        self.add_top_down_list(
            self.items, self.table_widget
        )  # Repopulate with all items


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Stores()
    mainWin.show()
    sys.exit(app.exec())
