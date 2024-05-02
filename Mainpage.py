import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QPushButton, QVBoxLayout,QStackedWidget,
                               QWidget)

import Basket
import Earning
import EditProfile
import Equipment
import LoginPage
import Stockes
import Stores


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.resize(1200, 600)
        self.initial_geometry = self.geometry()
        self.setWindowTitle("GRADUATION PROJECT")

        self.stacked_widget = QStackedWidget(self)

        self.open_earning_page_button = QPushButton("Go to First Page", self)
        self.open_earning_page_button.clicked.connect(self.open_first_page)
        self.open_earning_page_button.setStyleSheet("background-color: white;")
        self.stacked_widget.addWidget(self.open_earning_page_button)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        layout.addStretch(2)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(50)
        self.add_button("Equipment Prices", 0, 0, grid_layout, self.openequipment_Page)
        self.add_button("Stocks", 0, 1, grid_layout, self.openstockes_Page)
        self.add_button("Store", 1, 0, grid_layout, self.openStore_Page)
        self.add_button("Basket", 1, 1, grid_layout, self.openBasket_Page)
        #self.add_button("Earning", 2, 0, grid_layout, self.open_earning_page)

        

        layout.addLayout(grid_layout)
        layout.addStretch(2)

        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black
        self.show()

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
        button.setFixedWidth(400)
        button.setFixedHeight(70)
        layout.addWidget(button, row, col)

    def add_dynamic_label(self, text, layout):
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
        v_layout.addStretch(1)
        layout.addLayout(v_layout)

        label = QLabel(text, self)
        label.setStyleSheet(
            "font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(100)
        v_layout.addWidget(label)

        dropdown.currentIndexChanged.connect(self.dropdown_changed)

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openBasket_Page(self):
        self.hide()
        self.Basket = Basket.Basket(self.size())
        self.Basket.show()
        self.close()

    def openStore_Page(self):
        self.hide()
        self.Store = Stores.Stores(self.size())
        self.Store.show()
        self.close()

    def openequipment_Page(self):
        self.hide()
        self.Equipment = Equipment.EquipmentPrices(self.size())
        self.Equipment.show()
        self.close()

    def openstockes_Page(self):
        self.hide()
        self.Stockes = Stockes.Stocks(self.size())
        self.Stockes.show()
        self.close()

    def openEditProfile_Page(self):
        self.hide()
        self.Edit = EditProfile.EditProfile(self.size())
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.hide()
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()

    def open_earning_page(self):
        self.hide() 
        earning_page = Earning.Earning_page(self.size())  # Create an instance of the Earning_page
        self.earning_page.show()  # Show the Earning_page
        earning_page.resizeEvent = self.on_second_window_resize

    def on_second_window_resize(self, event):
        self.resize(event.size())

    def open_first_page(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec())