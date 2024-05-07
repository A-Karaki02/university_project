import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QWidget)

import LoginPage
import Mainpage
import SignupPage


class EditProfile(QWidget):
    def __init__(self,initial_size):
        super().__init__()
        self.resize(initial_size)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle("GRADUATION PROJECT")
        #self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_logo_label("BuildSmart", layout)
        layout.addStretch(2)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(1)
        grid_layout.setVerticalSpacing(20)
        grid_layout.setHorizontalSpacing(20)

        self.add_dynamic_label("Change Password :", grid_layout, 0, 0)
        self.add_textbox("Current Password", grid_layout, 1, 0)
        self.add_textbox("New Password", grid_layout, 2, 0)
        self.add_textbox("Confirm Password", grid_layout, 3, 0)
        self.add_dynamic_label("Personal Information :", grid_layout, 4, 0)
        self.add_textbox("First Name", grid_layout, 5, 0)
        self.add_textbox("Last Name", grid_layout, 6, 0)
        self.add_dynamic_label("Add debit/credit card :", grid_layout, 0, 5)
        self.add_textbox("Card Number", grid_layout, 1, 5)
        self.add_textbox("Card Name", grid_layout, 2, 5)
        self.add_textbox("CVV", grid_layout, 3, 5)
        self.add_button(
            "Save Changes return MainPage", 5, 5, grid_layout, self.openHome_Page
        )
        self.add_button("Back", 6, 5, grid_layout, self.openHome_Page)

        layout.addLayout(grid_layout)
        layout.addStretch(2)

        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black
        self.show()

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

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

    def dropdown_changed(self, index):
        if index == 2:  # Sign Out
            self.openLoginPage_Page()

    def add_textbox(self, label_text, layout, row, col):
        h_layout = QHBoxLayout()

        label = QLabel(label_text, self)
        label.setStyleSheet("font-size: 18px;color: rgb(0, 0, 0);font-weight: bold;")
        label.setFixedWidth(100)
        h_layout.addWidget(label)

        textbox = QLineEdit(self)
        textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);"
        )
        textbox.setFixedHeight(35)
        textbox.setFixedWidth(300)
        textbox.setPlaceholderText(label_text)

        layout.addWidget(label, row, col)  # Label at (row, column)
        layout.addWidget(textbox, row, col)

    def add_dynamic_label(self, text, layout, row, col):
        label = QLabel(text)
        label.setStyleSheet(
            "font-size: 18px;color: rgb(140, 140, 140); ;font-style: italic;font-weight: bold;"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(35)
        label.setFixedWidth(300)
        layout.addWidget(label, row, col)

    def openHome_Page(self):
        self.Main = Mainpage.MainPage()
        self.Login_page.show()
        self.close()

    def openHome_Page(self):
        self.Edit = Mainpage.MainPage()
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EditProfile()
    sys.exit(app.exec())
