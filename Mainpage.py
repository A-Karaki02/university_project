import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (QApplication, QComboBox,
                               QGraphicsDropShadowEffect, QGridLayout,
                               QHBoxLayout, QLabel, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)

import Basket
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

        self.setGeometry(0, 0, 1200, 600)
        self.initial_geometry = self.geometry()
        self.setWindowTitle("BuildSmart")
        self.setWindowIcon(QIcon("icon.png"))

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        layout.addStretch(1)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(50)
        self.add_button("History", 0, 0, grid_layout, self.openequipment_Page)
        self.add_button("Stocks", 0, 1, grid_layout, self.openstockes_Page)
        self.add_button("Store", 1, 0, grid_layout, self.openStore_Page)
        self.add_button("Basket", 1, 1, grid_layout, self.openBasket_Page)
        # self.add_button("Earning", 2, 0, grid_layout, self.open_earning_page)

        layout.addLayout(grid_layout)
        layout.addStretch(1)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")  # Black
        self.show()

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
        )  # White
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(135, 206, 250))
        shadow.setOffset(5, 5)

        # Apply shadow to button
        button.setGraphicsEffect(shadow)

        button.setFixedWidth(450)
        button.setFixedHeight(70)
        layout.addWidget(button, row, col)

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

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openBasket_Page(self):
        self.main_page_size = self.size()
        self.hide()
        self.Basket = Basket.Basket_page()
        self.Basket.resize(self.main_page_size or self.size())
        self.Basket.show()

    def openStore_Page(self):
        self.main_page_size = self.size()
        self.hide()
        self.Store = Stores.Stores()
        self.Store.resize(self.main_page_size or self.size())
        self.Store.show()

    def openequipment_Page(self):
        self.main_page_size = self.size()
        self.hide()
        self.Equipment = Equipment.EquipmentPrices()
        self.Equipment.resize(self.main_page_size or self.size())
        self.Equipment.show()

    def openstockes_Page(self):
        self.main_page_size = self.size()
        self.hide()
        self.Stockes = Stockes.Stocks()
        self.Stockes.resize(self.main_page_size or self.size())
        self.Stockes.show()

    def openEditProfile_Page(self):
        self.main_page_size = self.size()
        self.hide()
        self.Edit = EditProfile.EditProfile()
        self.Edit.resize(self.main_page_size or self.size())
        self.Edit.show()

    def openLoginPage_Page(self):
        self.login = LoginPage.LoginPage()
        self.login.show()
        self.close()

    def store_current_size(self):
        self.stored_geometry = self.geometry()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec())
