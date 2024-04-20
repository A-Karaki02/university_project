import hashlib
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QWidget)

import db
import LoginPage


class signup_page(QWidget):
    def __init__(self):
        super().__init__()
        self.__first_name = ""
        self.__last_name = ""
        self.__username = ""
        self.__email = ""
        self.__password = ""
        self.__phone_number = ""
        self.dtbs = db.firebase.database()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GRADUATION PROJECT")
        self.setFixedSize(QSize(1200, 600))

        # the label for the Title
        self.label_build_smart = QLabel("BuildSmart", self)
        self.label_build_smart.setGeometry(0, 50, 1200, 100)
        self.label_build_smart.setStyleSheet(
            "font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;"
        )  # Gray text on gray background
        self.label_build_smart.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # the textbox for First Name
        self.first_name_textbox = QLineEdit(self)
        self.first_name_textbox.setGeometry(450, 250, 125, 30)
        self.first_name_textbox.setPlaceholderText("First Name")
        self.first_name_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for last Name
        self.last_name_textbox = QLineEdit(self)
        self.last_name_textbox.setGeometry(625, 250, 125, 30)
        self.last_name_textbox.setPlaceholderText("Last Name")
        self.last_name_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for User Name
        self.username_textbox = QLineEdit(self)
        self.username_textbox.setGeometry(450, 300, 300, 30)
        self.username_textbox.setPlaceholderText("User Name")
        self.username_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Email
        self.email_textbox = QLineEdit(self)
        self.email_textbox.setGeometry(450, 350, 300, 30)
        self.email_textbox.setPlaceholderText("Email")
        self.email_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Phone Number
        self.phone_number_textbox = QLineEdit(self)
        self.phone_number_textbox.setGeometry(450, 400, 300, 30)
        self.phone_number_textbox.setPlaceholderText("Phone Number")
        self.phone_number_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Password
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setGeometry(450, 450, 300, 30)
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Confirm Password
        self.confirm_password_textbox = QLineEdit(self)
        self.confirm_password_textbox.setGeometry(450, 500, 300, 30)
        self.confirm_password_textbox.setPlaceholderText("Confirm Password")
        self.confirm_password_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the button for Sign Up
        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.setGeometry(625, 550, 125, 30)
        self.signup_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White
        self.signup_button.clicked.connect(self.openLoginPage)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(450, 550, 125, 30)
        self.back_button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
        self.back_button.clicked.connect(self.openLoginPage)

        # the label for the contact
        self.contact_label = QLabel(
            "Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111",
            self,
        )
        self.contact_label.setGeometry(50, 500, 200, 100)
        self.contact_label.setStyleSheet("color: rgb(140, 140, 140);")  # gray

        # Set background color using RGB for the window
        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black

        self.show()

    def handle_signup_click(self):
        # Get user input from text boxes
        self.__first_name = self.first_name_textbox.text()
        self.__last_name = self.last_name_textbox.text()
        self.__password = self.password_textbox.text()
        self.__phone_number = self.phone_number_textbox.text()
        self.__username = self.username_textbox.text()
        self.__email = self.email_textbox.text()

    def push_data_to_database(self):
        self.handle_signup_click()
        user_info = {
            "UserName": self.__username,
            "FirstName": self.__first_name,
            "LastName": self.__last_name,
            "PhoneNumber": self.__phone_number,
            "Email": self.__email,
            "Password": self.__password,
        }

        self.dtbs.child("Users").push(user_info)

    def openLoginPage(self):
        self.push_data_to_database()

        self.loginPage = LoginPage.login_page()
        self.loginPage.show()
        self.close()


# checking with isort

# a function to hash the password **********************************************************
# def hash_password(password):
#     # """Hash the password ."""
#     return hashlib.sha3_512(password.encode()).hexdigest()

# a function to save the inputs *******************************************************************************
# def sign_up():
#     # """Sign up a new user."""
#     F_Name =
#     L_Name =
#     Email =
#     phone_number =
#     username =

# The commented code below is commented because at the moment it doesnt work ********************************************************

# if user_exists(username):
#     print("Username already exists. Try a different one.")
#     return
