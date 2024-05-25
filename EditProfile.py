import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (QApplication, QComboBox,
                               QGraphicsDropShadowEffect, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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

        self.setWindowTitle("BuildSmart")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(0, 0, 1200, 600)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(1)
        grid_layout.setVerticalSpacing(20)
        grid_layout.setHorizontalSpacing(20)

        self.add_dynamic_labels("Personal Information :", grid_layout, 0, 0)
        self.textbox_first_name = QLineEdit(self)
        self.textbox_first_name.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        self.textbox_first_name.setFixedHeight(35)
        self.textbox_first_name.setFixedWidth(300)
        self.textbox_first_name.setPlaceholderText("First Name")
        grid_layout.addWidget(self.textbox_first_name, 1, 0)

        self.textbox_last_name = QLineEdit(self)
        self.textbox_last_name.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        self.textbox_last_name.setFixedHeight(35)
        self.textbox_last_name.setFixedWidth(300)
        self.textbox_last_name.setPlaceholderText("Last Name")
        grid_layout.addWidget(self.textbox_last_name, 1, 1)

        self.textbox_user_name = QLineEdit(self)
        self.textbox_user_name.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        self.textbox_user_name.setFixedHeight(35)
        self.textbox_user_name.setFixedWidth(300)
        self.textbox_user_name.setPlaceholderText("User Name")
        grid_layout.addWidget(self.textbox_user_name, 2, 0)

        self.textbox_Store_name = QLineEdit(self)
        self.textbox_Store_name.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        self.textbox_Store_name.setFixedHeight(35)
        self.textbox_Store_name.setFixedWidth(300)
        self.textbox_Store_name.setPlaceholderText("Store Name")
        grid_layout.addWidget(self.textbox_Store_name, 2, 1)

        self.textbox_phone_number = QLineEdit(self)
        self.textbox_phone_number.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        self.textbox_phone_number.setFixedHeight(35)
        self.textbox_phone_number.setFixedWidth(300)
        self.textbox_phone_number.setPlaceholderText("Phone Number")
        grid_layout.addWidget(self.textbox_phone_number, 3, 0)

        self.add_dynamic_labels("Add debit/credit card :", grid_layout, 4, 0)
        textbox_card_number = QLineEdit(self)
        textbox_card_number.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        textbox_card_number.setFixedHeight(35)
        textbox_card_number.setFixedWidth(300)
        textbox_card_number.setPlaceholderText("Card Number")
        grid_layout.addWidget(textbox_card_number, 5, 0)

        textbox_card_name = QLineEdit(self)
        textbox_card_name.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        textbox_card_name.setFixedHeight(35)
        textbox_card_name.setFixedWidth(300)
        textbox_card_name.setPlaceholderText("Card Name")
        grid_layout.addWidget(textbox_card_name, 6, 0)

        textbox_cvv = QLineEdit(self)
        textbox_cvv.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )
        textbox_cvv.setFixedHeight(35)
        textbox_cvv.setFixedWidth(300)
        textbox_cvv.setPlaceholderText("CVV")
        grid_layout.addWidget(textbox_cvv, 7, 0)

        self.add_button(
            "Change Password", 5, 1, grid_layout, self.handle_password_changes
        )
        self.add_button(
            "Save Changes return MainPage", 6, 1, grid_layout, self.save_changes
        )

        self.add_button("Back", 7, 1, grid_layout, self.back_button)

        layout.addLayout(grid_layout)
        layout.addStretch(2)

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
                            color : rgb(255,255,255);
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
        shadow.setColor(QColor(135, 206, 250))
        shadow.setOffset(5, 5)
        button.setFixedWidth(300)
        button.setFixedHeight(35)
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
            "font-size: 18px;color: rgb(10, 22, 39); ;font-style: italic;font-weight: bold;"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(35)
        label.setFixedWidth(300)
        layout.addWidget(label, row, col)

    def handle_password_changes(self):
        user.passwordReset("")

    def handle_save_changes(self):
        firstname = self.textbox_first_name.text().strip()
        lastname = self.textbox_last_name.text().strip()
        username = self.textbox_user_name.text().strip()
        phonenumber = self.textbox_phone_number.text().strip()
        storename = self.textbox_Store_name.text().strip()
        user.edit_user(firstname, lastname, username, phonenumber, storename)

    def save_changes(self):
        self.handle_save_changes()
        self.main = Mainpage.MainPage()
        self.main.setGeometry(self.geometry())  # Set geometry to match current window
        self.main.show()
        self.close()

    def back_button(self):
        self.main = Mainpage.MainPage()
        self.main.setGeometry(self.geometry())  # Set geometry to match current window
        self.main.show()
        self.close()

    def openLoginPage_Page(self):
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditProfile()
    window.show()
    sys.exit(app.exec())
