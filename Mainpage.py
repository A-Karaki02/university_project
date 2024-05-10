import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout,QSpacerItem,QSizePolicy,
                               QHBoxLayout, QLabel, QPushButton, QVBoxLayout,
                               QWidget)

import Basket
import Earning
import EditProfile
import Equipment
import LoginPage
import Stockes
import Stores
from UserManager import user


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setGeometry(100,100,1200,600)
        self.initial_geometry = self.geometry()
        self.setWindowTitle("GRADUATION PROJECT")

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        layout.addStretch(2)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(50)
        self.add_button("Equipment Prices", 0, 0, grid_layout, self.openequipment_Page)
        self.add_button("Stocks", 0, 1, grid_layout, self.openstockes_Page)
        self.add_button("Store", 1, 0, grid_layout, self.openStore_Page)
        self.add_button("Basket", 1, 1, grid_layout, self.openBasket_Page)
        self.add_button("Earning", 2, 0, grid_layout, self.open_earning_page)

        layout.addLayout(grid_layout)
        layout.addStretch(2)

        self.setStyleSheet("background-color: rgb(255, 255, 255);font-weight: bold;")  # Black
        self.show()

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(131, 170,229);font-weight: bold;")  # White
        button.setFixedWidth(400)
        button.setFixedHeight(70)
        layout.addWidget(button, row, col)

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
        spacer = QSpacerItem( 40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
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

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openBasket_Page(self):
        self.Basket = Basket.Basket_page()
        self.Basket.show()
        self.close()

    def openStore_Page(self):
        self.Store = Stores.Stores()
        self.Store.show()
        self.close()

    def openequipment_Page(self):
        self.Equipment = Equipment.EquipmentPrices()
        self.Equipment.show()
        self.close()

    def openstockes_Page(self):
        self.Stockes = Stockes.Stocks()
        self.Stockes.show()
        self.close()

    def openEditProfile_Page(self):
        self.Edit = EditProfile.EditProfile()
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()

    def open_earning_page(self):
        self.Earning = Earning.Earning_page()
        self.SignOut.show()
        self.close()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec())
