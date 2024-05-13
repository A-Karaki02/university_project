import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy,QSpacerItem,QVBoxLayout, QWidget)

import LoginPage
import Mainpage
import SignupPage
from UserManager import user


class EditProfile(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)
        

        grid_layout = QGridLayout()
        grid_layout.setSpacing(1)
        grid_layout.setVerticalSpacing(20)
        grid_layout.setHorizontalSpacing(20)

        self.add_dynamic_labels("Change Password :", grid_layout, 0, 0)
        self.add_textbox("Current Password", grid_layout, 1, 0)
        self.add_textbox("New Password", grid_layout, 2, 0)
        self.add_textbox("Confirm Password", grid_layout, 3, 0)
        self.add_dynamic_labels("Personal Information :", grid_layout, 4, 0)
        self.add_textbox("First Name", grid_layout, 5, 0)
        self.add_textbox("Last Name", grid_layout, 6, 0)
        self.add_dynamic_labels("Add debit/credit card :", grid_layout, 0, 5)
        self.add_textbox("Card Number", grid_layout, 1, 5)
        self.add_textbox("Card Name", grid_layout, 2, 5)
        self.add_textbox("CVV", grid_layout, 3, 5)
        self.add_button(
            "Save Changes return MainPage", 5, 5, grid_layout, self.openHome_Page
        )
        self.add_button("Back", 6, 5, grid_layout, self.openHome_Page)

        layout.addLayout(grid_layout)
        layout.addStretch(2)

        self.setStyleSheet("background-color: rgb(255, 255, 255);font-weight: bold;")  # Black
        self.show()

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(131, 170,229);font-weight: bold;border: 2px solid black;border-radius: 10px;box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);")  # White
        button.setFixedWidth(300)
        button.setFixedHeight(35)
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
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        textbox.setFixedHeight(35)
        textbox.setFixedWidth(300)
        textbox.setPlaceholderText(label_text)

        layout.addWidget(label, row, col)  # Label at (row, column)
        layout.addWidget(textbox, row, col)

    def add_dynamic_labels(self, text, layout, row, col):
        label = QLabel(text)
        label.setStyleSheet(
            "font-size: 18px;color: rgb(0, 0, 0); ;font-style: italic;font-weight: bold;"
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



