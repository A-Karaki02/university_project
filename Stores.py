import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QLineEdit, QPushButton, QVBoxLayout, QWidget)

import AddStore
import EditProfile
import LoginPage
import Mainpage


class Stores(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_logo_label("BuildSmart", layout)
        layout.addStretch(2)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)
        self.add_button("Add", 0, 5, grid_layout, self.openAddStorePage)

        self.add_button("Back", 100, 0, grid_layout, self.openMain_Page)
        self.add_button("Done", 100, 5, grid_layout, self.openMain_Page)

        self.add_button("test", 0, 0, grid_layout, self.test)

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

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

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

    def test(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Stores()
    sys.exit(app.exec())
