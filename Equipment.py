import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,QTableWidgetItem,QTableWidget,QGraphicsDropShadowEffect,
                               QHBoxLayout,QSpacerItem,QSizePolicy,QLineEdit,QCheckBox,QHeaderView,
                               QPushButton, QVBoxLayout, QWidget)
from PySide6.QtGui import QColor
import EditProfile
import LoginPage
import Mainpage
import SignupPage
from UserManager import user


class EquipmentPrices(QWidget):
    def __init__(self):
        super().__init__()
      
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        table_widget = QTableWidget()

        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        
        items = [
            {"storeName": "Store A", "itemName": "Item 1", "itemType": "Type X", "price": 10, "quantity": 2, "profit_paid": "Profit"},
            {"storeName": "Store B", "itemName": "Item 2", "itemType": "Type Y", "price": 20, "quantity": 3, "profit_paid": "Paid"},
            {"storeName": "Store C", "itemName": "Item 3", "itemType": "Type Z", "price": 30, "quantity": 1, "profit_paid": "Profit"}
        ]
        self.add_top_down_list(items, table_widget, layout)
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)
        self.add_button("Back", 0, 0, grid_layout, self.openMain_Page)
        self.add_button("Done", 0, 2, grid_layout, self.openMain_Page)
        self.switch_function("Sorted By Paid", 0, 1, grid_layout)

        

        # Set the layout
        self.setLayout(layout)

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
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

    def switch_function(self, button_text, row, col, layout):
        switch_button = QPushButton(button_text, self)

        # Initial state and text
        switch_state = 0
        switch_text = ["Sorted By Paid","Sorted By Profit", "Random"]
        switch_button.setFixedWidth(300)
        switch_button.setFixedHeight(35)
        def on_switch_clicked():
            nonlocal switch_state
            switch_state = (switch_state + 1) % 3
            switch_button.setText(switch_text[switch_state])
            print(f"{switch_text[switch_state]} clicked")
        
        switch_button.clicked.connect(on_switch_clicked)  # Connect the clicked signal to the function
        switch_button.setStyleSheet("background-color: rgb(131, 170,229);font-weight: bold;border: 2px solid black;border-radius: 10px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);")  # White
        layout.addWidget(switch_button, row, col)

    def add_top_down_list(self, items, table_widget, layout):
        headers = [
            "Store Name",
            "Item Name",
            "Item Type",
            "Price",
            "Quantity",
            "Total",
            "Profit/Paid"
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
            table_widget.setItem(table_widget.rowCount() - 1, 0, QTableWidgetItem(item.get("storeName", "")))
            table_widget.setItem(table_widget.rowCount() - 1, 1, QTableWidgetItem(item.get("itemName", "")))
            table_widget.setItem(table_widget.rowCount() - 1, 2, QTableWidgetItem(item.get("itemType", "")))

            # Set price and quantity
            for col, header_text in enumerate(["Price", "Quantity"], start=3):
                item_value = item.get(header_text.lower(), "")
                table_item = QTableWidgetItem(str(item_value))
                table_item.setFlags(table_item.flags() ^ Qt.ItemIsEditable)  # Make cell non-editable
                table_widget.setItem(table_widget.rowCount() - 1, col, table_item)
                table_item.setForeground(Qt.black)  # Set text color to black for all columns

            # Calculate total
            price = float(item.get("price", 0))
            quantity = float(item.get("quantity", 0))
            total = price * quantity
            table_widget.setItem(table_widget.rowCount() - 1, 5, QTableWidgetItem(str(total)))

            # Set profit/paid and adjust text color
            profit_paid = item.get("profit_paid", "")
            table_item = QTableWidgetItem(str(profit_paid))
            if profit_paid == "Paid":
                table_item.setForeground(Qt.red)
            elif profit_paid == "Profit":
                table_item.setForeground(Qt.green)
            table_item.setFlags(table_item.flags() ^ Qt.ItemIsEditable)  # Make cell non-editable
            table_widget.setItem(table_widget.rowCount() - 1, 6, table_item)

            # Set the background color of the row to white
            for col in range(len(headers)):
                if table_widget.item(table_widget.rowCount() - 1, col) is not None:
                    table_widget.item(table_widget.rowCount() - 1, col).setBackground(QColor(235, 235, 235))

        # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black;font-size: 16px;")

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

    def test(self):
        pass
