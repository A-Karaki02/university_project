import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox,
                               QGraphicsDropShadowEffect, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)

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
        self.layout = QVBoxLayout(self)
        self.table_widget = QTableWidget()

        self.setWindowTitle("BuildSmart")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(0, 0, 1200, 600)

        self.layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", self.layout)

        items = user.fetch_history()
        self.add_top_down_list(items, self.table_widget)
        self.layout.addWidget(self.table_widget)

        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)
        self.add_button("Back", 0, 0, grid_layout, self.openMain_Page)
        self.switch_function("Show All", 0, 1, grid_layout)

        # Set the layout
        self.setLayout(self.layout)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.show()

    def add_dynamic_label(self, text, layout):
        layout_widget = QWidget(self)
        layout_widget.setStyleSheet("background-color: rgb(10,22,39);")

        v_layout = QVBoxLayout(layout_widget)

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
        h_layout.addItem(spacer)

        dropdown = QComboBox(self)
        dropdown.addItems([user.get_username(), "Edit Profile", "Sign Out"])
        dropdown.setStyleSheet(
            "background-color: rgb(10,22,39); color: rgb(255, 255, 255);border: 0px solid black;"
        )
        dropdown.setFixedHeight(30)
        dropdown.setFixedWidth(120)
        h_layout.addWidget(dropdown)
        v_layout.addLayout(h_layout)

        layout.addWidget(layout_widget)

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
            color:rgb(255,255,255);
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
        button.setFixedHeight(35)
        button.setFixedWidth(300)
        layout.addWidget(button, row, col)

    def switch_function(self, button_text, row, col, layout):
        switch_button = QPushButton(button_text, self)

        # Initial state and text
        self.switch_state = 0
        self.switch_text = ["Show All", "Show Paid", "Show Profit"]
        switch_button.setFixedWidth(300)
        switch_button.setFixedHeight(35)

        def on_switch_clicked():
            self.switch_state = (self.switch_state + 1) % 3
            switch_button.setText(self.switch_text[self.switch_state])
            self.update_table_content(self.switch_text[self.switch_state])

        switch_button.clicked.connect(on_switch_clicked)
        switch_button.setStyleSheet(
            "background-color: rgb(10,22,39);color:rgb(255,255,255);font-weight: bold;border: 2px solid black;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);"
        )
        layout.addWidget(switch_button, row, col)

    def update_table_content(self, filter_type):
        items = user.fetch_history()
        if filter_type == "Show Paid":
            items = [item for item in items if item.get("isPurchased", False)]
        elif filter_type == "Show Profit":
            items = [item for item in items if not item.get("isPurchased", False)]
        self.add_top_down_list(items, self.table_widget)

    def add_top_down_list(self, items, table_widget):
        table_widget.clearContents()
        table_widget.setRowCount(0)
        headers = [
            "Store Name",
            "Item Name",
            "Item Type",
            "Price",
            "Quantity",
            "Total",
            "Profit/Paid",
            "Date",
            "Time",
        ]
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()
        header.setStyleSheet("background-color: rgb(10,22,39);")
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setVisible(False)

        for item in items:
            if not item:
                continue
            table_widget.insertRow(table_widget.rowCount())

            table_widget.setItem(
                table_widget.rowCount() - 1,
                0,
                QTableWidgetItem(item.get("storeName", "")),
            )
            table_widget.setItem(
                table_widget.rowCount() - 1,
                1,
                QTableWidgetItem(item.get("itemName", "")),
            )
            table_widget.setItem(
                table_widget.rowCount() - 1,
                2,
                QTableWidgetItem(item.get("itemType", "")),
            )

            for col, header_text in enumerate(["Price", "Quantity"], start=3):
                item_value = item.get(header_text.lower(), "")
                table_item = QTableWidgetItem(str(item_value))
                table_item.setFlags(table_item.flags() ^ Qt.ItemIsEditable)
                table_widget.setItem(table_widget.rowCount() - 1, col, table_item)
                table_item.setForeground(Qt.black)

            price = float(item.get("price", 0))
            quantity = float(item.get("quantity", 0))
            total = price * quantity
            table_widget.setItem(
                table_widget.rowCount() - 1, 5, QTableWidgetItem(str(total))
            )

            is_purchased = item.get("isPurchased", False)
            profit_paid = "Paid" if is_purchased else "Profit"
            table_item = QTableWidgetItem(profit_paid)
            table_item.setForeground(Qt.red if is_purchased else Qt.green)
            table_item.setFlags(table_item.flags() ^ Qt.ItemIsEditable)
            table_widget.setItem(table_widget.rowCount() - 1, 6, table_item)

            date_time = item.get("time", "").split(" ")
            date = date_time[0] if len(date_time) > 0 else ""
            time = date_time[1] if len(date_time) > 1 else ""
            table_widget.setItem(table_widget.rowCount() - 1, 7, QTableWidgetItem(date))
            table_widget.setItem(table_widget.rowCount() - 1, 8, QTableWidgetItem(time))

            for col in range(len(headers)):
                if table_widget.item(table_widget.rowCount() - 1, col) is not None:
                    table_widget.item(table_widget.rowCount() - 1, col).setBackground(
                        QColor(235, 235, 235)
                    )

        table_widget.setStyleSheet("border: 2px solid black;font-size: 16px;")

    def openMain_Page(self):
        self.main = Mainpage.MainPage()
        self.main.setGeometry(self.geometry())  # Set geometry to match current window
        self.main.show()
        self.close()

    def dropdown_changed(self, index):
        if index == 1:
            self.openEditProfile_Page()
        elif index == 2:
            self.openLoginPage_Page()

    def openEditProfile_Page(self):
        self.Edit = EditProfile.EditProfile()
        self.Edit.setGeometry(self.geometry())  # Set geometry to match current window
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.login = LoginPage.LoginPage()
        self.login.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentPrices()
    sys.exit(app.exec())
